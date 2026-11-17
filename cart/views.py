from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, CartItem
from products.models import Products


def get_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        # Create a session if it doesn't exist
        if not request.session.session_key:
            request.session.create()
        # Get the guest user's session ID
        session_key = request.session.session_key
        # Get existing guest cart or create a new one
        cart, created = Cart.objects.get_or_create(session_key=session_key)

    # Return the user's cart
    return cart


def add_to_cart(request, product_id):

    product = get_object_or_404(Products, id=product_id)
    cart = get_cart(request)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart")


def cart(request):

    # Get the user's cart
    cart = get_cart(request)

    # Get all products inside the cart
    cart_items = CartItem.objects.filter(cart=cart)

    # Send cart items to HTML page
    return render(request, "cart/cart.html", {"cart_items": cart_items})
