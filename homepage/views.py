from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import sqlite3

DB_PATH = 'data/trpf.sqlite'


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'homepage/index.html')


def statistics(request: HttpRequest) -> HttpResponse:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    offers_to_suppliers: list[sqlite3.Row] = conn.execute(
        """
        SELECT
            suppliers.supplier_id,
            suppliers.name,
            COUNT(offers.offer_id) as count_offers
        FROM suppliers
        LEFT JOIN offers ON suppliers.supplier_id = offers.supplier_id
        GROUP BY suppliers.supplier_id, suppliers.name
        ORDER BY suppliers.supplier_id;
        """
    ).fetchall()

    offers_to_products: list[sqlite3.Row] = conn.execute(
        """
        SELECT
            products.product_id,
            products.name,
            COUNT(offers.offer_id) as count_offers
        FROM products
        LEFT JOIN offers ON products.product_id = offers.product_id
        GROUP BY products.product_id, products.name
        ORDER BY products.product_id;
        """
    ).fetchall()

    count_offers: sqlite3.Row | None = conn.execute(
        """
        SELECT
            COUNT(*) as count_offers
        FROM offers;
        """
    ).fetchone()

    count_suppliers: sqlite3.Row | None = conn.execute(
        """
        SELECT
            COUNT(*) as count_suppliers
        FROM suppliers;
        """
    ).fetchone()

    count_users: sqlite3.Row | None = conn.execute(
        """
        SELECT
            COUNT(*) as count_users
        FROM users;
        """
    ).fetchone()

    count_products: sqlite3.Row | None = conn.execute(
        """
        SELECT
            COUNT(*) as count_products
        FROM products;
        """
    ).fetchone()

    conn.close()

    context: dict[str, list[sqlite3.Row] | sqlite3.Row | None] = {
        'offers_to_suppliers': offers_to_suppliers,
        'offers_to_products': offers_to_products,
        'count_offers': count_offers,
        'count_suppliers': count_suppliers,
        'count_users': count_users,
        'count_products': count_products
    }

    return render(request, 'homepage/statistics.html', context)


def page_not_found(request: HttpRequest, exception: Exception) -> HttpResponse:
    return render(
        request,
        '404.html',
        status=404,
    )
