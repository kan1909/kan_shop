from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.carts.models import Cart
from utils.random_str import random_String

User = get_user_model()


class OrderPhysical(models.Model):
    PAYMENT_CHOICES = (
        ('Банковские переводы на расчетный счёт', 'Банковские переводы на расчетный счёт'),
        ('Перевод на карту', 'Перевод на карту')
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="orders_ph", null=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.CharField(max_length=255)
    order_id = models.CharField(max_length=15, unique=True)
    payment_type = models.CharField(max_length=255, choices=PAYMENT_CHOICES)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0, null=True)

    class Meta:
        verbose_name = 'Заказ Физический'
        verbose_name_plural = 'Заказы Физические'
        ordering = ('-id',)

    def __str__(self):
        return f"order {self.order_id}"


class Product(models.Model):
    order_phys = models.ForeignKey(
        OrderPhysical, on_delete=models.CASCADE,
        related_name='product_order_phys',
    )
    title = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name='Наименование товара',
        db_index=True,
    )
    description = models.TextField(
        blank=True, null=True,
        verbose_name='Описание'
    )
    price = models.DecimalField(
        max_digits=20, decimal_places=2, default=0,
        verbose_name='Стоимость',
    )
    size_chart = models.CharField(
        max_length=255, blank=True, null=True,
        verbose_name='Размерная сетка'
    )
    size = models.CharField(
        max_length=255, blank=True, null=True,
        verbose_name='Размер'
    )
    color = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name='Цвет', db_index=True,
    )
    amount = models.PositiveIntegerField(
        verbose_name='Количество'
    )
    image = models.ImageField(
        upload_to='products_order',
        verbose_name='Изображение',
    )

    def __str__(self):
        return f'{self.title} -- {self.price}'


class OrderEntity(models.Model):
    PAYMENT_CHOICES = (
        ('Банковские переводы на расчетный счёт', 'Банковские переводы на расчетный счёт'),
        ('Перевод на карту', 'Перевод на карту')
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="orders_en", null=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.CharField(max_length=255)
    order_id = models.CharField(max_length=15, unique=True)
    payment_type = models.CharField(max_length=255, choices=PAYMENT_CHOICES)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    inn = models.CharField(max_length=255)
    kpp = models.CharField(max_length=255)
    contact_face = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0, null=True)

    class Meta:
        verbose_name = 'Заказ Юридическое лицо'
        verbose_name_plural = 'Заказ Юридические лица'
        ordering = ('-id',)

    def __str__(self):
        return f"order {self.order_id}"


class ProductEntity(models.Model):
    order_entity = models.ForeignKey(
        OrderEntity, on_delete=models.CASCADE,
        related_name='product_order_entity',
    )
    title = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name='Наименование товара',
        db_index=True,
    )
    description = models.TextField(
        blank=True, null=True,
        verbose_name='Описание'
    )
    price = models.DecimalField(
        max_digits=20, decimal_places=2, default=0,
        verbose_name='Стоимость',
    )
    size_chart = models.CharField(
        max_length=255, blank=True, null=True,
        verbose_name='Размерная сетка'
    )
    size = models.CharField(
        max_length=255, blank=True, null=True,
        verbose_name='Размер'
    )
    color = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name='Цвет', db_index=True,
    )
    amount = models.PositiveIntegerField(
        verbose_name='Количество'
    )
    image = models.ImageField(
        upload_to='products_order',
        verbose_name='Изображение',
    )

    def __str__(self):
        return f'{self.title} -- {self.price}'


@receiver(pre_save, sender=OrderPhysical)
def pre_save_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = random_String()


@receiver(pre_save, sender=OrderEntity)
def pre_save_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = random_String()
