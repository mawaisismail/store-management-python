import json
from django.shortcuts import render
from .models import ProductsModel
from django.http import Http404, HttpResponse


def products_page(request):
    try:
        products = ProductsModel.objects.all()
        return render(request, 'products.html', {"products": products})
    except Exception as e:
        raise Http404("Something went wrong")


def products_detail_page(request, product_id):
    try:
        product = ProductsModel.objects.get(id=product_id)
        return render(request, 'product-detail.html', {"product": product})
    except Exception:
        raise Http404("Something went wrong")


def shopping_cart_page(request):
    return render(request, 'shopping-cart.html')


def add_to_cart(request, product_id):
    print(product_id)
    return HttpResponse("Something went wrong", status=400)
