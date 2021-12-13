from rest_framework import serializers

from apps.favorites.models import Favorite
from apps.products.serializers import ProductItemSerializer


class FavoriteSerializer(serializers.ModelSerializer):
    products = ProductItemSerializer(many=True, read_only=True)

    class Meta:
        model = Favorite
        fields = "__all__"


class FavoriteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('products',)
