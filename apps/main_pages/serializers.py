from rest_framework import serializers
from apps.main_pages.models import MainPage
from apps.categories.serializers import CategoryListSerializer


class MainPageSerializer(serializers.ModelSerializer):
    categories = CategoryListSerializer(read_only=True)

    class Meta:
        model = MainPage
        fields = "__all__"


class MainPageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPage
        fields = (
            'title', 'image', 'categories',
        )
