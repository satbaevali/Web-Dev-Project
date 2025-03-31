from django.contrib import admin

from .models import Category,Product,ProductManager,Manager

admin.site.register(ProductManager)
admin.site.register(Product)
admin.site.register(Category)

admin.site.register(Manager)

