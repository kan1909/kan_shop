from rest_framework.routers import DefaultRouter
from apps.main_pages import views


router = DefaultRouter()
router.register('', views.MainPageViewSet, basename='main_pages')

urlpatterns = router.urls
