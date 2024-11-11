from django.apps import AppConfig
from django.contrib import admin

from carts.models import Cart

admin.site.register(Cart)
