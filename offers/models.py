from django.db import models


class Offer(models.Model):
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        related_name='offers'
    )

    supplier = models.ForeignKey(
        'suppliers.Supplier',
        on_delete=models.CASCADE,
        related_name='offers'
    )

    price = models.FloatField()
    min_lots = models.FloatField()
    delivery_time_days = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Предложение"
        verbose_name_plural = "Предложения"


    def __str__(self) -> str:
        return f'Предложение {self.id}'
