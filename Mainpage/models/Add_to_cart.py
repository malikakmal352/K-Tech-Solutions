from itertools import product

from django.db import models
from Mainpage.models.Customer import customer
from Mainpage.models.Products import Product

class addtocart(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    Total = models.PositiveIntegerField(default=0)

    def save(self):
        pro = Product.objects.filter(id=self.product.id)
        for io in pro:
            Price = io.price
        self.Total = self.quantity * Price
        super(addtocart, self).save()


    def __str__(self):
        return self.customer.email