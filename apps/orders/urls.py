from django.urls import path

from apps.orders import views

urlpatterns = [
    path('phys/', views.OrderPhysicalListCreateView.as_view(), name='order-phys-list-create'),
    path('phys/<int:pk>/', views.OrderPhysicalView.as_view(), name='order-phys-detail'),
    path('entity/', views.OrderEntityListCreateView.as_view(), name='order-entity-list-create'),
    path('entity/<int:pk>/', views.OrderEntityView.as_view(), name='order-entity-detail'),
    path('order_phis_history/', views.CartPhysicalHistory.as_view(), name='order-phis-history'),
    path('order_entity_history/', views.CartEntityHistory.as_view(), name='order-entity-history')
]
