from django.contrib import admin
from .models import CategoriesModel, ProductsModel


class AdminProducts(admin.ModelAdmin):
    list_display = ('name', 'price', 'category_id')  # Add more fields as needed

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category_id":
            kwargs["queryset"] = CategoriesModel.objects.all()
            kwargs["to_field_name"] = "name"  # Display the name in the dropdown
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(CategoriesModel)
class AdminCategories(admin.ModelAdmin):
    pass


@admin.register(ProductsModel)
class AdminProductsModel(AdminProducts):
    pass
