from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.db import models


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":
        return redirect("/")


def signup(request):
    return render(request, 'signup.html')
