from django.contrib import admin
from .models import Category
from .models import Customer
from .models import Product
from .models import Order


# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
