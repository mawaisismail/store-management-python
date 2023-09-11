from django.shortcuts import render
from .models import ProductsModel, CartModel
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
    products = CartModel.objects.filter(user_id=request.user)
    print(products)
    return render(request, 'shopping-cart.html', {'products': products})


def add_to_cart(request, product_id):
    products_item = ProductsModel.objects.get(id=product_id)
    try:
        product = CartModel.objects.get(user_id=request.user, product_id=products_item)
        product.quantity += 1
        product.save()
    except CartModel.DoesNotExist:
        CartModel.objects.create(user_id=request.user, product_id=products_item)

    return HttpResponse("Added to cart successfully")


def order_page(request):
    return render(request, 'order.html')
