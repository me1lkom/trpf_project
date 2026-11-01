from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    inn = models.CharField(max_length=12, unique=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    def __str__(self) -> str:
        return self.name


class SupplierMember(models.Model):
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name='members'
    )

    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='membership'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['supplier', 'user'],
                name='unique_supplier_member'
            )
        ]
        verbose_name = "Работник поставщика"
        verbose_name_plural = "Работники поставщика"

    def __str__(self) -> str:
        return f'{self.user} — {self.supplier}'
