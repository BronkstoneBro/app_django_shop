from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context: dict = {
        'title': 'Home',
        'content': 'Welcome to the homepage - HOME',
        'list': ['first', 'second',],
        'dict': {'first': 1},
        'is_auth': False,
    }

    return render(request, "main/index.html", context)


def about(request):
    return HttpResponse("This is the about page.")
