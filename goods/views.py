from django.shortcuts import render

from goods.models import Products


def catalog(request):

    goods = Products.objects.all()
    context: dict = {
        'title': 'Home - Каталог',
        'goods': goods,
    }

    return render(request, "goods/catalog.html", context)


def product(request):
    context: dict[str, str] = {
        'title': 'Home - Товар',
        'content': 'Товар',
    }
    return render(request, "goods/product.html", context)
