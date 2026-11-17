from django.contrib import admin
from .models import Cart, CartItem


# Register your models here.
class CartCustom(admin.ModelAdmin):
    list_display = ("user",)


class CartItemCustom(admin.ModelAdmin):
    list_display = ("cart", "product", "quantity")


admin.site.register(Cart, CartCustom)
admin.site.register(CartItem, CartItemCustom)
