from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import sqlite3

DB_PATH = 'data/trpf.sqlite'


def supplier_list(request: HttpRequest) -> HttpResponse:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    suppliers: list[sqlite3.Row] = conn.execute(
        """
        SELECT
            supplier_id,
            name,
            inn,
            phone,
            email
        FROM suppliers
        ORDER BY name;
        """
    ).fetchall()
    conn.close()

    context: dict[str, list[sqlite3.Row]] = {
        'suppliers': suppliers,
    }

    return render(request, "suppliers/supplier_list.html", context)


def supplier_details(request: HttpRequest, supplier_id: int) -> HttpResponse:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    supplier: sqlite3.Row | None = conn.execute(
        """
        SELECT
            supplier_id,
            name,
            inn,
            phone,
            email
        FROM suppliers
        WHERE supplier_id = ?;
        """,
        (supplier_id,)
    ).fetchone()

    offers: list[sqlite3.Row] = conn.execute(
        """
        SELECT
            offers.offer_id,
            offers.price,
            offers.min_lots,
            offers.delivery_time_days,
            products.name as product_name,
            products.description as product_description,
            products.country as product_country,
            COALESCE(users.name, suppliers.name) as buyers_name,
            CASE
                WHEN product_buyers.user_id IS NOT NULL
                    THEN 'Физ лицо'
                WHEN product_buyers.supplier_id IS NOT NULL
                    THEN 'Организация'
            END AS buyers_type
        FROM offers
        JOIN products ON products.product_id = offers.product_id
        LEFT JOIN product_buyers ON
            product_buyers.product_id = products.product_id
        LEFT JOIN users ON
            product_buyers.user_id = users.user_id
        LEFT JOIN suppliers ON
            product_buyers.supplier_id = suppliers.supplier_id
        WHERE offers.supplier_id = ?;
        """,
        (supplier_id,)
    ).fetchall()

    conn.close()

    context: dict[str, sqlite3.Row | None | list[sqlite3.Row]] = {
        'supplier': supplier,
        'offers': offers
    }

    return render(
        request,
        'suppliers/supplier_detail.html',
        context,
        status=404 if supplier is None else 200,
    )
