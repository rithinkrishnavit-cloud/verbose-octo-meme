from django.db import models
from django.contrib.auth.models import User
from products.models import Products

# Create your models here.


# Cart tells us who owns the cart.
# One Cart belongs to one User.
# A guest cart belongs to a session instead of a User.
class Cart(models.Model):

    # OneToOneField creates a relationship between
    # User and Cart tables.
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    # Stores the guest user's session ID.
    session_key = models.CharField(max_length=40, null=True, blank=True, unique=True)

    def __str__(self):
        if self.user:
            return self.user.username
        return self.session_key


# CartItem tells us what products are inside the cart.
class CartItem(models.Model):

    # Connects CartItem with Cart.
    # One Cart can contain multiple CartItems.
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    # Connects CartItem with your existing Products model.
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    # Stores the selected product quantity.
    # Default quantity is 1.
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name
