from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context: dict = {
        'title': 'Home - Главная',
        'content': 'Магазин Мебели Home',
    }

    return render(request, "main/index.html", context)


def about(request):
    context: dict = {
        'title': 'Home - О Нас',
        'content': 'О Нас',
        'text_on_page': 'test text',
    }

    return render(request, "main/about.html", context)
