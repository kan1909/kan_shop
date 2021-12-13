from rest_framework import serializers
from .models import Cart, CartItem
from apps.products.serializers import ProductItemSerializer


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('id', 'amount', 'product_item')


class CartItemDetailSerializer(serializers.ModelSerializer):
    product_item = ProductItemSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ('id', 'amount', 'product_item')


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Cart
        fields = ('id', 'user', 'cart_items',)
