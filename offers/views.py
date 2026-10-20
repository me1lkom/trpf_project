from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import sqlite3

DB_PATH = 'data/trpf.sqlite'


def offer_list(request: HttpRequest) -> HttpResponse:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    offers: list[sqlite3.Row] = conn.execute(
        """
        SELECT
            offers.offer_id,
            offers.price,
            offers.min_lots,
            offers.delivery_time_days,
            products.name as product_name,
            suppliers.name as supplier_name
        FROM offers
        JOIN products ON products.product_id = offers.product_id
        JOIN suppliers ON suppliers.supplier_id = offers.supplier_id
        ORDER BY offers.offer_id;
        """
    ).fetchall()

    conn.close()

    context: dict[str, list[sqlite3.Row]] = {
        'offers': offers,
    }

    return render(request, "offers/offer_list.html", context)


def offer_details(request: HttpRequest, offer_id: int) -> HttpResponse:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    offer: sqlite3.Row | None = conn.execute(
        """
        SELECT
            offers.offer_id,
            offers.price,
            offers.min_lots,
            offers.delivery_time_days,
            products.name as product_name,
            products.description as product_description,
            products.country as product_country,
            suppliers.name as supplier_name,
            suppliers.inn as supplier_inn,
            suppliers.phone as supplier_phone,
            suppliers.email as supplier_email,
            COALESCE(buyers_users.name, buyers_suppliers.name) as buyers_name,
            CASE
                WHEN product_buyers.user_id IS NOT NULL
                    THEN 'Физ лицо'
                WHEN product_buyers.supplier_id IS NOT NULL
                    THEN 'Организация'
            END AS buyers_type
        FROM offers
        JOIN products ON products.product_id = offers.product_id
        JOIN suppliers ON suppliers.supplier_id = offers.supplier_id
        LEFT JOIN product_buyers ON
            product_buyers.product_id = products.product_id
        LEFT JOIN users AS buyers_users ON
            product_buyers.user_id = buyers_users.user_id
        LEFT JOIN suppliers AS buyers_suppliers ON
            product_buyers.supplier_id = buyers_suppliers.supplier_id
        WHERE offers.offer_id = ?;
        """,
        (offer_id,)
    ).fetchone()

    conn.close()

    context: dict[str, sqlite3.Row | None] = {
        'offer': offer
    }

    return render(
        request,
        "offers/offer_detail.html",
        context,
        status=404 if offer is None else 200
    )
