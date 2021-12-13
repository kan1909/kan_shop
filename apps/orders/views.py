import re

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.celery_tasks import send_order

from apps.orders.models import OrderEntity, OrderPhysical, Product, ProductEntity
from apps.orders.serializers import (
    OrderEntitySerializer,
    OrderPhysicalSerializer,
    ProductPhysicalOrderSerializer,
    ProductEntityOrderSerializer
)


class OrderPhysicalListCreateView(generics.ListCreateAPIView):
    queryset = OrderPhysical.objects.all()
    serializer_class = OrderPhysicalSerializer

    def perform_create(self, serializer):
        user = self.request.user
        summa = 0
        data_product = []
        for item in user.cart.cart_items.all():
            json_data = {}
            product_item = item.product_item
            json_data['title'] = product_item.title
            json_data['price'] = product_item.price
            json_data['size_chart'] = product_item.size_chart
            json_data['size'] = product_item.size
            json_data['color'] = product_item.color
            image_data = product_item.products_image.first()
            correct_image = re.sub('/media', "", image_data.image.url)
            json_data['image'] = correct_image
            json_data['amount'] = item.amount
            json_data['description'] = product_item.description
            data_product.append(json_data)
            summa += product_item.price * item.amount
            product_item.quantity -= item.amount
            product_item.save()
            item.delete()

        serializer.save(
            user=user,
            cart=user.cart,
            total=summa,
        )
        send_order.delay(user.email, serializer.data['order_id'], data_product, summa)

        for i in data_product:
            save_prod = Product(order_phys_id=serializer.data['id'])
            save_prod.title = i['title']
            save_prod.price = i['price']
            save_prod.size_chart = i['size_chart']
            save_prod.size = i['size']
            save_prod.color = i['color']
            save_prod.image = i['image']
            save_prod.amount = i['amount']
            save_prod.description = i['description']
            save_prod.save()


class OrderPhysicalView(generics.RetrieveAPIView):
    queryset = OrderPhysical.objects.all()
    serializer_class = OrderPhysicalSerializer


class OrderEntityListCreateView(generics.ListCreateAPIView):
    queryset = OrderEntity.objects.all()
    serializer_class = OrderEntitySerializer

    def perform_create(self, serializer):
        user = self.request.user
        summa = 0
        data_product = []
        for item in user.cart.cart_items.all():
            json_data = {}
            product_item = item.product_item
            json_data['title'] = product_item.title
            json_data['price'] = product_item.price
            json_data['size_chart'] = product_item.size_chart
            json_data['size'] = product_item.size
            json_data['color'] = product_item.color
            json_data['image'] = product_item.products_image.all()
            image_data = product_item.products_image.first()
            correct_image = re.sub('/media', "", image_data.image.url)
            json_data['image'] = correct_image
            json_data['amount'] = item.amount
            json_data['description'] = product_item.description
            data_product.append(json_data)
            summa += product_item.price * item.amount
            product_item.quantity -= item.amount
            product_item.save()
            item.delete()

        serializer.save(
            user=user,
            cart=user.cart,
            total=summa,
        )
        send_order.delay(user.email, serializer.data['order_id'])

        for i in data_product:
            save_prod = ProductEntity(order_entity_id=serializer.data['id'])
            save_prod.title = i['title']
            save_prod.price = i['price']
            save_prod.size_chart = i['size_chart']
            save_prod.size = i['size']
            save_prod.color = i['color']
            save_prod.image = i['image']
            save_prod.amount = i['amount']
            save_prod.description = i['description']
            save_prod.save()


class OrderEntityView(generics.RetrieveAPIView):
    queryset = OrderEntity.objects.all()
    serializer_class = OrderEntitySerializer


class CartPhysicalHistory(APIView):
    """Get product history"""

    def get(self, request, *args, **kwargs):
        try:
            order = OrderPhysical.objects.filter(user=self.request.user)[0]
            product_data = order.product_order_phys.all()
            serializer = ProductPhysicalOrderSerializer(product_data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response({"detail": "CartPhysicalHistory Is Empty."})


class CartEntityHistory(APIView):
    """Get product history"""

    def get(self, request, *args, **kwargs):
        try:
            order = OrderEntity.objects.filter(user=self.request.user)[0]
            product_data = order.product_order_entity.all()
            serializer = ProductEntityOrderSerializer(product_data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response({"detail": "CartEntityHistory Is Empty."})
