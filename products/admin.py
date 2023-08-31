from django.contrib import admin
from .models import CategoriesModel, ProductsModel, CartModel


@admin.register(CategoriesModel)
class AdminCategories(admin.ModelAdmin):
    pass


@admin.register(ProductsModel)
class AdminProductsModel(admin.ModelAdmin):
    pass


@admin.register(CartModel)
class AdminCartModel(admin.ModelAdmin):
    pass
