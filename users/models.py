from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return self.name
