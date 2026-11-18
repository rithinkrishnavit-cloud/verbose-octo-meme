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
        print("Session Key:", request.session.session_key)
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

    cart = get_cart(request)

    cart_items = CartItem.objects.filter(cart=cart)

    total = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, "cart/cart.html", {"cart_items": cart_items, "total": total})


def remove_from_cart(request, item_id):

    # Get the selected cart item
    cart_item = get_object_or_404(CartItem, id=item_id)

    # Delete the cart item
    cart_item.delete()

    # Return to cart page
    return redirect("cart")
