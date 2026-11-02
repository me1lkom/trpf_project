from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    country = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Продукт"

    def __str__(self) -> str:
        return str(self.name)


class ProductBuyers(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='buyer_record'
    )

    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='user_buyer'
    )

    supplier = models.ForeignKey(
        'suppliers.Supplier',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='supplier_buyer'
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=(
                    ((models.Q(user__isnull=False)) &
                     (models.Q(supplier__isnull=True)))
                    |
                    ((models.Q(user__isnull=True)) &
                     (models.Q(supplier__isnull=False)))
                ),
                name='one_product_buyer'
            )
        ]
        verbose_name = "Покупатель"
        verbose_name_plural = "Пользователи"
