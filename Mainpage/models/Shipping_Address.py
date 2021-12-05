from django.db import models
from Mainpage.models.Customer import customer
from Mainpage.models.order import order
from Mainpage.models.Products import Product


class shippingAddress(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=300, null=False)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    zipcode = models.CharField(max_length=50, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address




