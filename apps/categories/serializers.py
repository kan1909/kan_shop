from rest_framework import serializers
from apps.categories.models import Category
from rest_framework_recursive.fields import RecursiveField


class CategoryListSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = Category
        fields = (
            'id', 'title', 'name', 'parent',
            'children',
        )


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)

    class Meta:
        model = Category
        fields = (
            'id', 'title', 'name', 'parent',
        )
