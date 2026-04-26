# shop/views/cart.py

from django.shortcuts import render, redirect, get_object_or_404
from shop.models.product import Product

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('show_cart')

def show_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for pid, quantity in cart.items():
        product = get_object_or_404(Product, id=pid)
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })

    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('show_cart')
def decrease_cart_quantity(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    if product_id_str in cart:
        if cart[product_id_str] > 1:
            cart[product_id_str] -= 1
        else:
            del cart[product_id_str]
        request.session['cart'] = cart
    return redirect('show_cart')
