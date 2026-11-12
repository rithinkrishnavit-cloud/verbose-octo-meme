from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Products


# Create your views here.
def home(request):

    products = Products.objects.all()

    return render(request, "products/home.html", {"products": products})
