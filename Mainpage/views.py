from django.shortcuts import render
from Mainpage.models.Category_model import Category
from Mainpage.models.Products import Product
from .models.order import order, order_items

from .models.Shipping_Address import shippingAddress
from .models.Customer import customer


# Create your views here.

def mainindex(request):
    products = Product.objects.all()
    category = Category.get_all_Category()
    data = {'products': products, 'category': category}

    return render(request, "index.html", data)


def Add_cart(request):
    q = 0
    total = 0
    price = 0
    if request.user.is_authenticated:
        Customer = request.user.customer
        Order, created = order.objects.get_or_create(customer=Customer, complete_order=False)
        items = order_items.objects.all()
        for i in items:
            q = q+i.quantity
            if i.quantity > 1:
                price = i.product.price * i.quantity
                total = total + price
            else:
                total = total + i.product.price

    else:
        items = []
        


    data = {'items': items, 'order': order,'q': q, 'total': total}
    return render(request, "addcart.html", data)


def checkout(request):
    q = 0
    total = 0
    price = 0
    if request.user.is_authenticated:
        Customer = request.user.customer
        Order, created = order.objects.get_or_create(customer=Customer, complete_order=False)
        items = order_items.objects.all()
        for i in items:
            q = q + i.quantity
            if i.quantity > 1:
                price = i.product.price * i.quantity
                total = total + price
            else:
                total = total + i.product.price

    data = {'items': items, 'order': order,'q': q, 'total': total}
    return render(request, "Checkout.html", data)


def productView(request, id):
    product = Product.objects.get(id=id)
    data = {'product': product}
    return render(request, 'productview.html', data)
