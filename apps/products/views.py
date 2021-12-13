from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, mixins

from apps.products.models import Product, ProductImage, ProductItem, ProductSale
from apps.products.serializers import (
    ProductSerializer,
    ProductImageSerializer,
    ProductItemSerializer,
    ProductSaleSerializer,
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_fields = ['category']
    search_fields = ['article']


class ProductSaleAPIView(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    queryset = ProductSale.objects.all()
    serializer_class = ProductSaleSerializer


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class ProductItemViewSet(viewsets.ModelViewSet):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_fields = ['price']
    search_fields = [
        'title', 'size', 'color',
    ]
