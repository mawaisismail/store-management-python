from django.http import HttpResponse
from django.template.loader import get_template


def home_page(response):
    return HttpResponse(get_template("home.html").render())
