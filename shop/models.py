from django.db import models
from accounts.enums import ProductStatus, PurchaseStatus
from accounts.models import Profile
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=True)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=1, choices=[(s.name, s.value) for s in ProductStatus])

    def __str__(self):
        return f'{self.name}'


class Purchase(models.Model):
    consumer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='consumer', null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product', null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(unique=True)
    status = models.CharField(max_length=1, choices=[(s.name, s.value) for s in PurchaseStatus])

    def __str__(self):
        return f'{self.product.name}'
