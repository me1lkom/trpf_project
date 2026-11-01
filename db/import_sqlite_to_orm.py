import os
import sys
import sqlite3
from pathlib import Path

import django
from django.db import transaction


BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(BASE_DIR))

SOURCE_DB = BASE_DIR / "data" / "trpf.sqlite"

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings",
)

django.setup()

from users.models import User
from offers.models import Offer
from suppliers.models import Supplier, SupplierMember
from products.models import Product, ProductBuyers


def main():
    if not SOURCE_DB.exists():
        raise FileNotFoundError(
            f"Исходная база не найдена: {SOURCE_DB}"
        )

    with sqlite3.connect(SOURCE_DB) as connection:
        connection.row_factory = sqlite3.Row

        products = connection.execute(
            """
                SELECT
                    product_id,
                    name,
                    description,
                    country
                FROM products
                ORDER BY product_id
            """
        ).fetchall()

        suppliers = connection.execute(
            """
                SELECT
                    supplier_id,
                    name,
                    inn,
                    phone,
                    email
                FROM suppliers
                ORDER BY supplier_id
            """
        ).fetchall()

        offers = connection.execute(
            """
                SELECT
                    offer_id,
                    product_id,
                    supplier_id,
                    price,
                    min_lots,
                    delivery_time_days
                FROM offers
                ORDER BY offer_id
            """
        ).fetchall()

        users = connection.execute(
            """
                SELECT
                    user_id,
                    name,
                    email
                FROM users
                ORDER BY user_id
            """
        ).fetchall()

        product_buyers = connection.execute(
            """
                SELECT
                    product_id,
                    user_id,
                    supplier_id
                FROM product_buyers
                ORDER BY product_id
            """
        ).fetchall()

        supplier_members = connection.execute(
            """
                SELECT
                    user_id,
                    supplier_id
                FROM supplier_members
                ORDER BY user_id, supplier_id
            """
        ).fetchall()

        with transaction.atomic():

            for row in users:
                User.objects.update_or_create(
                    pk=row["user_id"],

                    defaults={
                        "name": row["name"],
                        "email": row["email"]
                    },
                )

            for row in suppliers:
                Supplier.objects.update_or_create(
                    pk=row["supplier_id"],

                    defaults={
                        "name": row["name"],
                        "inn": row["inn"],
                        "phone": row["phone"],
                        "email": row["email"]
                    },
                )

            for row in products:
                Product.objects.update_or_create(
                    pk=row["product_id"],

                    defaults={
                        "name": row["name"],
                        "description": row["description"],
                        "country": row["country"]
                    },
                )

            for row in offers:
                Offer.objects.update_or_create(
                    pk=row["offer_id"],

                    defaults={
                        "product_id": row["product_id"],
                        "supplier_id": row["supplier_id"],
                        "price": row["price"],
                        "min_lots": row["min_lots"],
                        "delivery_time_days": row["delivery_time_days"]
                    },
                )

            for row in supplier_members:
                SupplierMember.objects.update_or_create(
                    user_id=row["user_id"],
                    supplier_id=row["supplier_id"],
                )

            for row in product_buyers:
                ProductBuyers.objects.update_or_create(
                    product_id=row["product_id"],

                    defaults={
                        "user_id": row["user_id"],
                        "supplier_id": row["supplier_id"],
                    }
                )

    print("Перенос данных завершён.")
    print(f"Пользователей: {User.objects.count()}")
    print(f"Товаров: {Product.objects.count()}")
    print(f"Поставщики: {Supplier.objects.count()}")
    print(f"Предложений: {Offer.objects.count()}")
    print(f"Работники поставщиков: {SupplierMember.objects.count()}")
    print(f"Покупатели: {ProductBuyers.objects.count()}")
    
if __name__ == "__main__":
    main()