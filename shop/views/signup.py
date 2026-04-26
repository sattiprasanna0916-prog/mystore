from django.shortcuts import render,redirect
from django.http import HttpResponse
from shop.models.product import Product
from shop.models.category import Category
from django.contrib.auth.hashers import make_password,check_password
from shop.models.customer import Customer
from django.views import View
class signup(View):
    def get(self,request):
        return render(request,"signup.html")
    def post(self,request):
        fn=request.POST['fn']
        ln=request.POST['ln']
        email=request.POST['email']
        mobile=request.POST['mobile']
        password=request.POST['password']
        userdata=[fn,ln,email,password,mobile]
        print(userdata)
        uservalues={
            'fn':fn,
            'ln':ln,
            'email':email,
            'mobile':mobile,         
        }
        #storing object
        customerdata=Customer(first_name=fn,last_name=ln,email=email,mobile=mobile,password=password)
        #validation
        error_msg=None
        success_msg=None
        if(not fn):
            error_msg='First name should not be empty'
        elif(not ln):
            error_msg='last name should not be empty'
        elif(not email):
            error_msg='Email Id should not be empty'
        elif(not mobile):
            error_msg='Mobile no should not be empty'
        elif(not password):
            error_msg='password should not be empty'
        elif(customerdata.isexist()):
            error_msg='Email already Exists'
        if (not error_msg):
            customerdata.password=make_password(password)
            success_msg="Account created successfully"
            customerdata.save()
            msg={'success':success_msg}
            return render(request,'signup.html',msg)
        else:
            msgs={'error':error_msg,'value':uservalues}
            return render(request,'signup.html',msgs)

     
    
    