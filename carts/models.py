from django.db import models

from goods.models import Products
from users.models import User


class CartQuerySet(models.QuerySet):
    def total_price(self):
        return [cart.product_price() for cart in self]

    def total_quantity(self):
        return sum(cart.quantity for cart in self)

class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="Пользователь")
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name="Продукт")
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Количество")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    objects = CartQuerySet().as_manager()
    def product_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f"Корзина {self.product.name} | Товар {self.product.name} | Количество {self.quantity}"
