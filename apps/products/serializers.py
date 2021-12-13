from rest_framework import serializers

from apps.products.models import Product, ProductImage, ProductItem, ProductSale


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class ProductItemSerializer(serializers.ModelSerializer):
    products_image = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = ProductItem
        fields = "__all__"


class ProductSaleSerializer(serializers.ModelSerializer):
    product_item = ProductItemSerializer(read_only=True)

    class Meta:
        model = ProductSale
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    product_items = ProductItemSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
