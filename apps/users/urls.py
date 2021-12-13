from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.users import views

router = DefaultRouter()
router.register('', views.UserViewSet, basename='users')

urlpatterns = [
    path('current-user/', views.current_user, name='current_user'),
]

urlpatterns += router.urls
