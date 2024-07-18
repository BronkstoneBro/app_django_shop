from django.contrib import admin

from goods.models import Categories, Products


# admin.site.register(Categories)
# admin.site.register(Product)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
