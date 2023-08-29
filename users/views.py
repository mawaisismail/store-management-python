from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserForgetPassword


def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if confirm_password != password:
            return render(request, "signup.html")
        user = User.objects.filter(username=email).exists()
        if user:
            return render(request, "signup.html")
        new_user = User.objects.create_user(email=email, password=password, username=email, first_name=first_name,
                                            last_name=last_name)
        new_user.save()
        print(new_user)
        return redirect("/user/login")


def login_user(request):
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            print(user)
            login(request, user)
            return redirect('/')
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required
def change_password(request):
    form = UserForgetPassword()
    return render(request, "change-password.html", {"form": form})
