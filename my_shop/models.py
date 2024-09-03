from django.db import models
import datetime 


# Create your models here.
class Category(models.Model): 
    name = models.CharField(max_length=50) 

class Customer(models.Model): 
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50) 
    phone = models.CharField(max_length=10) 
    email = models.EmailField() 
    password = models.CharField(max_length=100) 
  

class Product(models.Model): 
    name = models.CharField(max_length=60) 
    price = models.IntegerField(default=0) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1) 
    description = models.CharField(max_length=250, default='', blank=True, null=True) 
  
class Order(models.Model): 
    product = models.ForeignKey(Product, 
                                on_delete=models.CASCADE) 
    customer = models.ForeignKey(Customer, 
                                 on_delete=models.CASCADE) 
    quantity = models.IntegerField(default=1) 
    price = models.IntegerField() 
    address = models.CharField(max_length=50, default='', blank=True) 
    phone = models.CharField(max_length=50, default='', blank=True) 
    date = models.DateField(default=datetime.datetime.today) 
    status = models.BooleanField(default=False) 
  