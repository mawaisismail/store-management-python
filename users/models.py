from django.db import models
from django.contrib.auth.models import User


class UserBilling(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    landmark = models.CharField(max_length=200)
