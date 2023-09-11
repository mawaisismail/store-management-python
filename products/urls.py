from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_page),
    path('details/<product_id>', views.products_detail_page),
    path('add_to_cart/<int:product_id>', views.add_to_cart),
    path('cart', views.shopping_cart_page),
    path('order', views.order_page),
]
