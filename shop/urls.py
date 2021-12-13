"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from apps.users.views import TokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView, TokenVerifyView,
)

from apps.users.views import email_verify

schema_view = get_schema_view(
    openapi.Info(
        title="SAY-OPT-SHOP API",
        default_version="v1",
        description="API for SAY-OPT-SHOP",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="nursultandev@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

api_patterns = [
    path('users/', include('apps.users.urls')),
    path('categories/', include('apps.categories.urls')),
    path('products/', include('apps.products.urls')),
    path('mainpage/', include('apps.main_pages.urls')),
    path('newsletters/', include('apps.newsletters.urls')),
    path('favorites/', include('apps.favorites.urls')),
    path('carts/', include('apps.carts.urls')),
    path('orders/', include('apps.orders.urls')),

    # auth
    path('email-verify/<str:email>/', email_verify, name='verify_email'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # documentation
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui", ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc-ui"),

]

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_patterns)),
    path("auth/", include("rest_framework.urls")),
    path('api/password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
