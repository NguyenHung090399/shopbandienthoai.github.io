from django.shortcuts import render ,redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate , login , logout
from .form import RegistrationForm 
from django.http import JsonResponse
from .models import *
import json
# Create your views here.
def login_user(request) : 
    if request.method == 'POST' : 
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username = username , password = password)
        if user is not None : 
            login(request , user)
            return redirect('home')
        else : 
            return redirect('login')
    else :     
        return render(request , 'user/login.html')

def register(request) : 
    form = RegistrationForm()
    context = {'form' : form}
    if request.method == 'POST' : 
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        user = User.objects.create_user(username , email , password)
        Customer.objects.create(user = user , name = user.username , email = user.email , age = 18)
        user.save()
        return redirect('login')
    else :
        return render(request , 'user/register.html' , context)

def logout_user(request) : 
    logout(request)
    return redirect('home')

def home(request) : 
    category = Category.objects.filter()
    product_list = Product.objects.filter()

    if request.user.is_authenticated : # kiem tra user da duoc xac thu chua 
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer = customer , complete = False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_item
    else : 
        items = []
        customer = []
        order = {'get_cart_item' : 0 , 'get_cart_total' : 0}
        cartItem = order['get_cart_item']

    context = {'product_list' : product_list , 'category':category , 'cartItem':cartItem  , 'profile':customer }
    return render(request , 'app/home.html' , context)

def category(request , category_id) : 
    category = Category.objects.filter()
    product_list = Product.objects.filter(category = category_id)

    if request.user.is_authenticated : # kiem tra user da duoc xac thu chua 
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer = customer , complete = False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_item
    else : 
        items = []
        customer = []
        order = {'get_cart_item' : 0 , 'get_cart_total' : 0}
        cartItem = order['get_cart_item']


    context = {'product_list' : product_list , 'category':category ,  'cartItem':cartItem , 'profile':customer}
    return render(request , 'app/category.html' , context)
def cart(request) : 
    category = Category.objects.filter()
    if request.user.is_authenticated : # kiem tra user da duoc xac thu chua 
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer = customer , complete = False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_item
    else : 
        items = []
        customer = []
        order = {'get_cart_item' : 0 , 'get_cart_total' : 0}
        cartItem = order['get_cart_item']
    context = {'order':order , 'items' : items , 'category':category ,  'cartItem':cartItem , 'profile':customer}
    return render(request , 'app/cart.html' , context)
def checkout(request) : 
    category = Category.objects.filter()
    if request.user.is_authenticated : # kiem tra user da duoc xac thu chua 
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer = customer , complete = False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_item
    else : 
        items = []
        customer = []
        order = {'get_cart_item' : 0 , 'get_cart_total' : 0}
        cartItem = order['get_cart_item']

    context = {'order':order , 'items' : items , 'category':category ,  'cartItem':cartItem , 'profile':customer}
    return render(request , 'app/checkout.html' , context)

def updateItem(request) : 
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:' , action )
    print('Product:' , productId)


    customer = request.user.customer
    product = Product.objects.get(id  = productId)
    order , created = Order.objects.get_or_create(customer = customer , complete = False)

    orderItem , created = OrderItem.objects.get_or_create(order = order , product = product)
    
    if action == 'add' : 
        orderItem.quantity+=1
    elif action == 'remove' : 
        orderItem.quantity-=1
    orderItem.save()
    if orderItem.quantity <= 0 : 
        orderItem.delete()
    if action == 'delete' :
        orderItem.delete()
    return JsonResponse('added' , safe=False)

def detail_product(request , id) : 
    category = Category.objects.filter()
    product_list = Product.objects.filter()

    if request.user.is_authenticated : # kiem tra user da duoc xac thu chua 
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer = customer , complete = False)
        items = order.orderitem_set.all()
        cartItem = order.get_cart_item
    else : 
        items = []
        customer = []
        order = {'get_cart_item' : 0 , 'get_cart_total' : 0}
        cartItem = order['get_cart_item']

    context = {'product_list' : product_list , 'category':category , 'cartItem':cartItem  , 'profile':customer }
    return render(request , 'app/detail_product.html' , context)