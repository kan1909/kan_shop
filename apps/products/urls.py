from rest_framework.routers import DefaultRouter
from apps.products import views

router = DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('images', views.ProductImageViewSet, basename='images')
router.register('product_items', views.ProductItemViewSet, basename='product_items')
router.register('sale', views.ProductSaleAPIView, basename='product_sale')

urlpatterns = router.urls
