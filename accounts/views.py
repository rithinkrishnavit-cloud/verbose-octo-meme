from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.


# user register
def register(request):

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = User.objects.create_user(
            username=email, first_name=name, email=email, password=password
        )
        return redirect("home")
    return render(request, "accounts/register.html")


# usr login
def user_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            error = "Invalid email or password"
            return render(request, "accounts/login.html", {"error": error})
    return render(request, "accounts/login.html")


# user logout
def user_logout(request):
    logout(request)
    return redirect("register")
