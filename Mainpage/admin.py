from django.contrib import admin

# Register your models here.
from .models.Category_model import Category
from .models.Products import Product
from .models.Brand import Brand
from .models.order import order, order_items
from .models.Shipping_Address import shippingAddress
from .models.Customer import customer



class ProductView(admin.ModelAdmin):
    list_display = ['Laptop_name', "RAM", "Hard_disk", 'Product_Category', 'Product_Brand', 'price']


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product, ProductView)
admin.site.register(order)
admin.site.register(order_items)
admin.site.register(customer)
admin.site.register(shippingAddress)
