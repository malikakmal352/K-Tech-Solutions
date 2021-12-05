from datetime import datetime

from django.db import models
from Mainpage.models.Customer import customer
from Mainpage.models.Products import Product


class order(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_order = models.DateTimeField(default=datetime.now(), null=True)
    complete_order = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    # @property
    # def get_cart_total(self):
    #     orderitems = self.objects.all()
    #     print(orderitems)
    #     total = sum(item.get_total for item in orderitems)
    #     print(total)
    #     return total
    #
    # @property
    # def get_cart_items(self):
    #     orderitems = self.order_items.objects.all()
    #     total = sum(item.quantity for item in orderitems)
    #     return total


class order_items(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
