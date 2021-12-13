from rest_framework import viewsets, filters

from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer, CategoryListSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategoryListSerializer
    filter_backends = [
        filters.SearchFilter,
    ]
    search_fields = ['title']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return self.serializer_class
        return CategorySerializer
