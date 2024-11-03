from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# Vendor Model
class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True)
    
    class Meta:
        verbose_name_plural = "Vendors"
        
    def __str__(self):
        return self.user.username

# Product Category Model
class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)
    
    class Meta:
        verbose_name_plural = "Product Categories"
    
    def __str__(self):
        return self.title
    
# Product Model
class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    detail = models.TextField(null=True)
    price = models.FloatField()
    
    def __str__(self):
        return self.title
