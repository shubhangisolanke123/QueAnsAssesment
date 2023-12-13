from django.db import models
'''
Vendor Management System
Model Design: Create a model to store vendor information including name, contact
details, address, and a unique vendor code.
'''
# Create your models here.
# models.py
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=100)
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(null=True, blank=True)
    quality_rating = models.FloatField(null=True, blank=True)
    response_time = models.FloatField(null=True, blank=True) 
    fulfillment_rate = models.FloatField(null=True, blank=True)
 
    def __str__(self) -> str:
        return self.name
    
'''
Model Design: Track purchase orders with fields like PO number, vendor reference,
order date, items, quantity, and status.
'''
class PurchaseOrder(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    po_number = models.CharField(max_length=50)
    order_date = models.DateField()
    items = models.TextField(blank=True, null=True)  
    quantity = models.PositiveIntegerField(blank=True, null=True)
    status = models.CharField(max_length=20,blank=True, null=True)  

    def __str__(self):
        return self.vendor