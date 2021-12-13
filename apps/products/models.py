from django.db import models

from apps.categories.models import Category


class Product(models.Model):
    article = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name='Артикль',
        db_index=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='products', blank=True, null=True,
    )

    class Meta:
        verbose_name = 'Продукт Артикул'
        verbose_name_plural = 'Продукты Артикулы'
        ordering = ('-id',)

    def __str__(self):
        return f"{self.article}"


class InStockManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(quantity=0)


class ProductItemManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class ProductItem(models.Model):
    title = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name='Наименование товара',
        db_index=True,
    )
    price = models.DecimalField(
        max_digits=20, decimal_places=2, default=0,
        verbose_name='Стоимость',
    )
    description = models.TextField(
        blank=True, null=True,
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='product_items',
    )
    size_chart = models.CharField(
        max_length=255, blank=True, null=True,
        verbose_name='Размерная сетка'
    )
    size = models.CharField(
        max_length=255, blank=True, null=True,
        verbose_name='Размер'
    )
    quantity = models.PositiveIntegerField()
    color = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name='Цвет', db_index=True,
    )
    objects = ProductItemManager()
    instock = InStockManager()

    def __str__(self) -> str:
        return f'{self.title} -- {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('-id',)


class ProductImage(models.Model):
    image = models.ImageField(
        upload_to='products',
        verbose_name='Изображение',
    )
    product_item = models.ForeignKey(
        ProductItem, on_delete=models.CASCADE,
        related_name='products_image',
    )

    def __str__(self) -> str:
        return f'{self.product_item.product.article} image'


class ProductSale(models.Model):
    product_item = models.ForeignKey(
        ProductItem, on_delete=models.CASCADE,
        related_name='products_sale',
    )

    def __str__(self) -> str:
        return f'{self.product_item.product.article} {self.product_item.title}'

