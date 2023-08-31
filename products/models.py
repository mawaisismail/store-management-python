from django.contrib import admin
from django.db import models


# Create your models here.
class CategoriesModel(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class ProductsModel(models.Model):
    category_id = models.ForeignKey(CategoriesModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
