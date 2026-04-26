# views/checkout.py
from django.shortcuts import render, redirect
from django.views import View
from models.order import Order  # You need to create this model
from models.product import Product

class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        for product_id, quantity in cart.items():
            order = Order(customer=customer,
                          product=Product(id=product_id),
                          quantity=quantity,
                          price=Product.get_product_by_id(product_id).price,
                          address=address)
            order.save()
        request.session['cart'] = {}
        return redirect('cart')
