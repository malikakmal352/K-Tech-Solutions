from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render, redirect
from Mainpage.models.Category_model import Category
from Mainpage.models.Products import Product
from .models.order import order, order_items

from .models.Shipping_Address import shippingAddress
from .models.Customer import customer
from .models.Add_to_cart import addtocart


# Create your views here.

def mainindex(request):
    if request.method == 'POST':
        useremail = request.POST.get('email')
        prod = request.POST.get('p_id')
        p_id = Product.objects.get(id=prod)

        if useremail:
            user = customer.objects.get(email=useremail)

        Addcart = addtocart(customer=user, product=p_id, quantity=1)
        Addcart.save()

    products = Product.objects.all().order_by('-id')
    category = Category.get_all_Category()
    data = {'products': products, 'category': category}
    return render(request, "Index.html", data)


def Add_cart(request):
    q = 0
    total = 0
    price = 0
    if request.session.get('email'):
        Customer = request.session['id']
        addcart = addtocart.objects.filter(customer=Customer)
        if addcart:
            items = addtocart.objects.filter(customer=Customer)
            for i in addcart:
                q = q + i.quantity
                request.session['cart'] = q
                if i.quantity > 1:
                    price = i.product.price * i.quantity
                    total = total + price
                else:
                    total = total + i.product.price

        else:
            items = []
    else:
        items = []

    data = {'items': items, 'order': order, 'q': q, 'total': total}
    return render(request, "addcart.html", data)


def min_product(request, id):
    product = addtocart.objects.get(id=id)
    product.quantity = product.quantity - 1
    if product.quantity == 0:
        product.delete()
    else:
        product.save()
    print(product.quantity)
    return redirect(Add_cart)


def add_product(request, id):
    product = addtocart.objects.get(id=id)
    product.quantity = product.quantity + 1
    product.save()
    print(product.quantity)
    return redirect(Add_cart)


def checkout(request):
    q = 0
    total = 0
    price = 0
    if request.session.get('email'):
        Customer = request.session['id']
        addcart = addtocart.objects.filter(customer=Customer)
        if addcart:
            items = addtocart.objects.filter(customer=Customer)
            for i in addcart:
                q = q + i.quantity
                if i.quantity > 1:
                    price = i.product.price * i.quantity
                    total = total + price
                else:
                    total = total + i.product.price

        else:
            items = []
    else:
        items = []

    data = {'items': items, 'order': order, 'q': q, 'total': total}
    return render(request, "Checkout.html", data)


def productView(request, id):
    product = Product.objects.get(id=id)
    data = {'product': product}
    return render(request, 'productview.html', data)


# ################################## Login and registration System Start########################################

def registeruser(request):
    Data = request.POST
    fullname = Data.get('fullname')
    email = Data.get('email')
    password = Data.get('password')
    C_password = Data.get('C_password')
    phone = Data.get('Mn')
    # gender = Data.get('gender')
    print(fullname, email, password, C_password, phone)
    # Validations
    value = {
        'fullname': fullname,
        'email': email,
        'password': password,
        'C_password,': C_password,
        'phone': phone,
        # 'gender': gender
    }
    error_message = None
    Customer = customer(name=fullname, email=email, password=password, Mn=phone)

    if not fullname:
        error_message = "Fullname is Required."
    elif len(fullname) < 4:
        error_message = "Fullname must be 4 char long or more"
    elif len(password) < 8:
        error_message = "Password must be minimum 8 char long or more"
    elif password != C_password:
        error_message = 'Password and Comfort Password must be same'
    elif not phone:
        error_message = "Phone number is Required."
    elif len(phone) < 10:
        error_message = " Phone number must be 10 digit long "
    elif Customer.isExits():
        error_message = "Email Already Exits "
    # Saving
    if not error_message:
        Customer.password = make_password(Customer.password)
        Customer.save()
        # Customer = Customer.get_by_email(email)
        # request.session['id'] = Customer.id
        # print(request.session.id)
        # print(Customer.email, Customer.id)
        return redirect(mainindex)
    else:
        data = {
            'error': error_message,
            'Value': value
        }
        return render(request, 'Signup.html', data)


def Signup(request):
    if request.method == 'GET':
        return render(request, 'Signup.html')
    else:
        return registeruser(request)


def Login(request):
    if request.method == 'GET':
        return render(request, 'Login.html')
    else:
        print('view reach ')
        Data = request.POST
        email = Data.get('email')
        password = Data.get('password')

        # Validations
        Customer = customer.get_by_email(email)
        error_message = None

        if Customer:
            print(Customer.password)
            flag = check_password(password, Customer.password)
            print('pass not match', Customer)
            if flag:
                request.session['id'] = Customer.id
                fa = request.session['email'] = Customer.email
                request.session['phone'] = Customer.Mn
                # request.session['Address'] = Patient.Address
                request.session['fullname'] = Customer.name

                print('you are ', Customer)
                print('customer Login')
                return redirect(mainindex)
            else:
                error_message = "Email or Password Invalid......"
        else:
            error_message = "Email or Password Invalid......"

        return render(request, 'Login.html', {'error': error_message})


def Logout(request):
    request.session.clear()

    return redirect(mainindex)

# ################################## Login and registration System Code End ########################################
