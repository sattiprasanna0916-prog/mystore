from django.urls import path
from .import views 
from shop.views import cart
from django.urls import path
from .views.home import home
from .views.signup import signup
from .views.login import login
from shop.views.book_now import BookNowView

urlpatterns = [
    path('',home.as_view(), name='home'),
    path('signup',signup.as_view(),name='signup'),
    path('login',login.as_view(),name='login'),
    path('add-to-cart/<int:product_id>/', cart.add_to_cart, name='add_to_cart'),
    path('decrease-cart/<int:product_id>/', cart.decrease_cart_quantity, name='decrease_cart_quantity'),
path('cart/', cart.show_cart, name='show_cart'),
    path('remove-from-cart/<int:product_id>/', cart.remove_from_cart, name='remove_from_cart'),
path('book-now/<int:product_id>/', BookNowView.as_view(), name='book_now'),
]






    