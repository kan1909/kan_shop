from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.products.models import ProductItem

User = get_user_model()


class CartManager(models.Manager):

    def get_or_new(self, request):
        user = request.user
        cart_id = request.session.get('cart_id', None)
        if user is not None and user.is_authenticated:
            if user.cart:
                cart_obj = request.user.cart
            else:
                cart_obj = Cart.objects.get(pk=cart_id)
                cart_obj.user = user
                cart_obj.save()
            return cart_obj
        else:
            cart_obj = Cart.objects.get_or_create(pk=cart_id)
            cart_id = request.session['cart_id'] = cart_obj[0].id
            return cart_obj[0]


class Cart(models.Model):
    user = models.OneToOneField(
        User,
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='cart'
    )

    objects = CartManager()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        ordering = ('-id',)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product_item = models.ForeignKey(ProductItem, related_name='product_in_cart', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1, blank=True)

    def __str__(self):
        return f"{self.cart.id} = cart items"

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'
        ordering = ('-id',)


@receiver(post_save, sender=User)
def create_cart_for_user(sender, instance=None, created=False, **kwargs):
    if created:
        Cart.objects.get_or_create(user=instance)
