from django_rq import job
from datetime import datetime, timedelta
from django_rq.queues import get_queue


# @job
def print_hello():
    # queue = get_queue()
    # queue.enqueue(print_hello, timeout=100)
    print("Hello")


@job("awais")
def print_hello_awais():
    queue = get_queue()
    queue.enqueue(timedelta(seconds=100), print_hello_awais)
    print("Hello awais")
