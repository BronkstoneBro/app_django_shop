from django.apps import AppConfig
from django.contrib import admin

class CartsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carts'
    verbose_name = "Корзины"
