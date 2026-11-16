from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Products


# Create your views here.
def home(request):

    category = request.GET.get("category")

    if category:
        products = Products.objects.filter(category=category)
    else:
        products = Products.objects.all()

    return render(
        request,
        "products/home.html",
        {"products": products, "selected_category": category},
    )
