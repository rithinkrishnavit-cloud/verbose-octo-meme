from django.contrib import admin
from .models import Products


# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock", "category", "created_at")
    list_filter = ("category",)


admin.site.register(Products, ProductsAdmin)
