from django.shortcuts import render
from handlers.handler import print_hello_handler
from datetime import timedelta


def home_page(request):
    print_hello_handler("awais", timedelta(seconds=10))
    return render(request, 'home.html')
