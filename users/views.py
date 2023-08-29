from django.http import HttpResponse
from django.template.loader import get_template


def login_page(response):
    return HttpResponse(get_template("login.html").render())
