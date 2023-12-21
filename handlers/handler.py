from django_rq import get_queue
from datetime import timedelta


def print_name():
    print("Hello World")


def print_hello_handler(a: str, delay: timedelta):
    queue = get_queue(a)
    queue.enqueue_in(delay, print_name)
