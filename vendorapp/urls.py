# urls.py
from django.urls import path
from .views import (
    vendor_list_create,
    vendor_retrieve_update_delete,
    purchase_order_list_create,
    purchase_order_retrieve_update_delete,vendor_performance
)

urlpatterns = [
    path('vendors/', vendor_list_create, name='vendor-list-create'),
    path('vendors/<int:pk>/', vendor_retrieve_update_delete, name='vendor-retrieve-update-delete'),
    path('vendors/<int:vendor_id>/performance/', vendor_performance, name='vendor-performance'),
    path('purchase_orders/', purchase_order_list_create, name='purchase-order-list-create'),
    path('purchase_orders/<int:pk>/', purchase_order_retrieve_update_delete, name='purchase-order-retrieve-update-delete'),
]