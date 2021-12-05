from django.db import models
from Mainpage.models.Category_model import Category
from Mainpage.models.Brand import Brand


# Create your models here.
class Product(models.Model):
    Availability = (
        ('In Stock', 'In Stock'),
        ('Out of Stock', 'Out of Stock'),
    )
    Laptop_name = models.CharField(max_length=75)
    RAM = models.CharField(max_length=20, default="2GB")
    Hard_disk = models.CharField(max_length=30, default="128 HHD")
    Processer = models.FloatField(null=True)
    price = models.IntegerField(default=0)
    RRP = models.IntegerField(default=1)
    Save = models.IntegerField(default=1)
    status = models.CharField(max_length=200, null=True, choices=Availability, default='In Stock')
    Product_Category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    Product_Brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=1)
    Description = models.TextField(max_length=400, default='', null=True, blank=True)
    img = models.ImageField(upload_to='Products/')

    def save(self):
        self.Save = self.RRP - self.price
        super(Product, self).save()

    def __str__(self):
        return self.Laptop_name

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_product():
        return Product.objects.all()

    @staticmethod
    def get_all_product_by_category(Category_id):
        if Category_id:
            return Product.objects.filter(Product_Category=Category_id)
        else:
            return Product.get_all_product()
