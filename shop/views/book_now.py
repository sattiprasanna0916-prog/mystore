from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from shop.models.product import Product
from django.views import View

class BookNowView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        return render(request, 'book_now.html', {'product': product})

    def post(self, request, product_id):
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        product = get_object_or_404(Product, id=product_id)# In a real app, you'd process user data and save booking here
        return HttpResponse("Booking confirmed!")
