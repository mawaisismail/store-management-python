from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_page),
    path('details/<id>', views.products_detail_page),
]
