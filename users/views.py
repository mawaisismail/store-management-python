from django.http import HttpResponse
from django.template.loader import get_template


def login(response):
    return HttpResponse(get_template("login.html").render())


def signup(response):
    return HttpResponse(get_template("signup.html").render())
