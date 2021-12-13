from rest_framework.routers import DefaultRouter

from apps.categories import views

router = DefaultRouter()
router.register('', views.CategoryViewSet, basename='categories')

urlpatterns = router.urls
