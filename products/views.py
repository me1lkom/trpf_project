from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import sqlite3

DB_PATH = 'data/trpf.sqlite'


def product_list(request: HttpRequest) -> HttpResponse:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    products: list[sqlite3.Row] = conn.execute(
        """
        SELECT
            product_id,
            name,
            description,
            country
        FROM products
        ORDER BY product_id;
        """
    ).fetchall()
    conn.close()

    context: dict[str, list[sqlite3.Row]] = {
        'products': products,
    }

    return render(request, 'products/product_list.html', context)


def product_details(request: HttpRequest, product_id: int) -> HttpResponse:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    product: sqlite3.Row | None = conn.execute(
        """
        SELECT
            products.product_id,
            products.name,
            products.description,
            products.country,
            COALESCE(users.name, suppliers.name) as buyers_name,
            CASE
                WHEN product_buyers.user_id IS NOT NULL
                    THEN 'Физ лицо'
                WHEN product_buyers.supplier_id IS NOT NULL
                    THEN 'Организация'
            END AS buyers_type
        FROM products
        LEFT JOIN product_buyers
            ON product_buyers.product_id = products.product_id
        LEFT JOIN users
            ON product_buyers.user_id = users.user_id
        LEFT JOIN suppliers
            ON product_buyers.supplier_id = suppliers.supplier_id
        WHERE products.product_id = ?;
        """,
        (product_id,),
    ).fetchone()

    order_by = {
        'default': 'ORDER BY offers.offer_id',
        'price': 'ORDER BY offers.price',
        'delivery': 'ORDER BY offers.delivery_time_days ASC'
    }

    sort = request.GET.get('sort', 'default')
    sorting = order_by.get(sort, order_by['default'])

    query = f"""
        SELECT
            offers.offer_id,
            offers.price,
            offers.min_lots,
            offers.delivery_time_days,
            products.name as product_name,
            suppliers.name as supplier_name,
            suppliers.phone as supplier_phone
        FROM offers
        JOIN products ON products.product_id = offers.product_id
        JOIN suppliers ON suppliers.supplier_id = offers.supplier_id
        WHERE offers.product_id = ?
        {sorting};
        """

    offers: list[sqlite3.Row] = conn.execute(
        query,
        (product_id, )
    ).fetchall()

    price_stat: sqlite3.Row | None = conn.execute(
        """
        SELECT
            MIN(price) as min_price,
            MAX(price) as max_price,
            ROUND(AVG(price), 2) as avg_price
        FROM offers
        WHERE offers.product_id = ?;
        """,
        (product_id,),
    ).fetchone()

    conn.close()

    context: dict[str, sqlite3.Row | None | list[sqlite3.Row]] = {
        'product': product,
        'offers': offers,
        'price_stat': price_stat
    }

    return render(
        request,
        'products/product_detail.html',
        context,
        status=404 if product is None else 200,
    )
