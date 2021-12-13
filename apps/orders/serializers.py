from rest_framework import serializers

from apps.orders.models import OrderPhysical, OrderEntity, ProductEntity, Product


class OrderPhysicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPhysical
        fields = (
            'id',
            'user', 'cart',
            'fname', 'lname', 'email',
            'order_id', 'address', 'number',
            'city', 'comment', 'payment_type',
            'created', 'total',
        )
        read_only_fields = (
            'user', 'cart',
            'order_id', 'created', 'total',
        )


class ProductPhysicalOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductEntityOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductEntity
        fields = '__all__'


class OrderEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderEntity
        fields = (
            'id',
            'user', 'cart',
            'fname', 'lname', 'email',
            'order_id', 'address', 'number', 'payment_type',
            'city', 'comment', 'inn', 'kpp',
            'contact_face', 'created', 'total',
        )
        read_only_fields = (
            'user', 'cart',
            'order_id', 'created', 'total'
        )
