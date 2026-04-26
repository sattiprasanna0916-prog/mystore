# shop/models/booking.py
from django.db import models
from shop.models.product import Product

class Booking(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    booked_at = models.DateTimeField(auto_now_add=True)
