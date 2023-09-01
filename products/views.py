from django.shortcuts import render
from .models import ProductsModel
from django.db import transaction, DatabaseError


def products_page(request):
    try:
        products = ProductsModel.objects.all()
        print(products)
        return render(request, 'products.html', {"products": products})
    except DatabaseError:
        return render(request, 'products.html')


def products_detail_page(request, id):
    return render(request, 'product-detail.html')
