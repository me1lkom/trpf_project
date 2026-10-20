import json
from typing import Any, cast
from db.database import get_connection
import sqlite3

USERS_FILE = 'data/users.json'
SUPPLIERS_FILE = 'data/suppliers.json'
PRODUCTS_FILE = 'data/products.json'
OFFERS_FILE = 'data/offers.json'
PRODUCT_BUYERS_FILE = 'data/product_buyers.json'
SUPPLIER_MEMBERS_FILE = 'data/supplier_members.json'


def load_json(filename: str) -> list[dict[str, Any]]:
    with open(filename, encoding='utf-8') as file:
        return cast(list[dict[str, Any]], json.load(file))


def import_users(conn: sqlite3.Connection) -> None:
    users = load_json(USERS_FILE)
    conn.executemany(
        """
        INSERT INTO users(
            user_id,
            name,
            email
        )
        VALUES (?, ?, ?)
    """,
        [
            (
                user["id"],
                user["name"],
                user["email"],
            )
            for user in users
        ],
    )


def import_suppliers(conn: sqlite3.Connection) -> None:
    suppliers = load_json(SUPPLIERS_FILE)
    conn.executemany(
        """
        INSERT INTO suppliers(
            supplier_id,
            name,
            inn,
            phone,
            email
        )
        VALUES (?, ?, ?, ?, ?)
    """,
        [
            (
                supplier["id"],
                supplier["name"],
                supplier["inn"],
                supplier["phone"],
                supplier["email"],
            )
            for supplier in suppliers
        ],
    )


def import_products(conn: sqlite3.Connection) -> None:
    products = load_json(PRODUCTS_FILE)
    conn.executemany(
        """
        INSERT INTO products(
            product_id,
            name,
            description,
            country
        )
        VALUES (?, ?, ?, ?)
    """,
        [
            (
                product["id"],
                product["name"],
                product["description"],
                product["country"],
            )
            for product in products
        ],
    )


def import_offers(conn: sqlite3.Connection) -> None:
    offers = load_json(OFFERS_FILE)
    conn.executemany(
        """
        INSERT INTO offers(
            offer_id,
            product_id,
            supplier_id,
            price,
            min_lots,
            delivery_time_days
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """,
        [
            (
                offer["id"],
                offer["product_id"],
                offer["supplier_id"],
                offer["price"],
                offer["min_lots"],
                offer["delivery_time_days"],
            )
            for offer in offers
        ],
    )


def import_product_buyers(conn: sqlite3.Connection) -> None:
    product_buyers = load_json(PRODUCT_BUYERS_FILE)
    conn.executemany(
        """
        INSERT INTO product_buyers(
            product_id,
            user_id,
            supplier_id
        )
        VALUES (?, ?, ?)
    """,
        [
            (
                product_buyer["product_id"],
                product_buyer["user_id"],
                product_buyer["supplier_id"],
            )
            for product_buyer in product_buyers
        ],
    )


def import_supplier_members(conn: sqlite3.Connection) -> None:
    supplier_members = load_json(SUPPLIER_MEMBERS_FILE)
    conn.executemany(
        """
        INSERT INTO supplier_members(
            user_id,
            supplier_id
        )
        VALUES (?, ?)
    """,
        [
            (
                supplier_member["user_id"],
                supplier_member["supplier_id"],
            )
            for supplier_member in supplier_members
        ],
    )


def main() -> None:
    conn = get_connection()
    try:
        import_users(conn)
        import_suppliers(conn)
        import_products(conn)
        import_offers(conn)
        import_product_buyers(conn)
        import_supplier_members(conn)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
