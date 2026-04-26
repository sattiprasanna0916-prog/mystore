from django.shortcuts import render,redirect
from django.http import HttpResponse
from shop.models.product import Product
from shop.models.category import Category
from django.contrib.auth.hashers import make_password,check_password
from shop.models.customer import Customer
from django.views import View
#class based view
class home(View):
    def get(self,request):
        categories=Category.objects.all()
        categoryID=request.GET.get('category')
        if categoryID:
            products=Product.get_category_id(categoryID)
        else:
            products=Product.objects.all()
        data={'products':products,'categories':categories} 
        return render(request,'index.html',data)
    def post(self,request):
        pass