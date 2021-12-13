from django.contrib.auth import get_user_model
from django.db import models

from apps.products.models import ProductItem

User = get_user_model()


class Favorite(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='favorites'
    )
    products = models.ManyToManyField(
        ProductItem, related_name='favorites'
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
        ordering = ('-id',)

    def __str__(self):
        return f"{self.user.email} -- {self.products.title}"
