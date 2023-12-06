# urls.py
from django.urls import path
from .views import (
    vendor_list_create,
    vendor_retrieve_update_delete,
    purchase_order_list_create,
    purchase_order_retrieve_update_delete,vendor_performance,
    
    
)


urlpatterns = [
    path('vendors/', vendor_list_create, name='vendor-list-create'),
    path('vendors/<int:pk>/', vendor_retrieve_update_delete, name='vendor-retrieve-update-delete'),
    path('vendors/<int:vendor_id>/performance/', vendor_performance, name='vendor-performance'),
    path('purchase_orders/', purchase_order_list_create, name='purchase-order-list-create'),
    path('purchase_orders/<int:pk>/', purchase_order_retrieve_update_delete, name='purchase-order-retrieve-update-delete'),
    
]


'''
vendor API Endpoints:
● POST /api/vendors/: Create a new vendor.
● GET /api/vendors/: List all vendors.
● GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
● PUT /api/vendors/{vendor_id}/: Update a vendor's details.
● DELETE /api/vendors/{vendor_id}/: Delete a vendor.
'''

'''
purchase order API Endpoints:
● POST /api/purchase_orders/: Create a purchase order.
● GET /api/purchase_orders/: List all purchase orders with an option to filter by
vendor.
● GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
● PUT /api/purchase_orders/{po_id}/: Update a purchase order.
● DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.
'''
'''
API Endpoints:
● GET /api/vendors/{vendor_id}/performance: Retrieve a vendor's
'''