from django.shortcuts import render
from handlers.handler import print_hello, print_hello_awais
from django_rq import get_queue
from datetime import timedelta


def home_page(request):
    queue = get_queue('default')
    queue.enqueue_in(timedelta(seconds=20), print_hello)
    # print_hello.delay()
    return render(request, 'home.html')
