from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    categories = Categories.objects.all()

    context: dict = {
        'title': 'Home - Главная',
        'content': 'Магазин Мебели Home',
        'categories': categories,
    }

    return render(request, "main/index.html", context)


def about(request):
    context: dict = {
        'title': 'Home - О Нас',
        'content': 'О Нас',
        'text_on_page': 'test text',
    }

    return render(request, "main/about.html", context)
