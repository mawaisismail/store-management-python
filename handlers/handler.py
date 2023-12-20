from django_rq import job


@job
def print_hello():
    print("Hello")


@job("awais")
def print_hello_awais():
    print("Hello awais")
