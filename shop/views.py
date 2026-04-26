from django.shortcuts import redirect,get_object_or_404
from .models import Product
def add_to_cart(request,product_id):
    product=get_object_or_404(Product,id=product_id)
    cart=request.session.get('cart',{})
    cart[str(product_id)]=cart.get(str(product_id),0)+1
    request.session['cart']=cart
    return redirect('show_cart')
def remove_from_cart(request,product_id):
    cart=request.session.get('cart',{})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart']=cart
    return redirect('show_cart')
def decrease_cart_quantity(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        if cart[str(product_id)] > 1:
            cart[str(product_id)] -= 1
        else:
            del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('show_cart')
    