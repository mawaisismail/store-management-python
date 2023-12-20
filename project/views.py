from django.shortcuts import render
from handlers.handler import print_hello,print_hello_awais

def home_page(request):
    print_hello.delay()
    print_hello_awais.delay()
    return render(request, 'home.html')
