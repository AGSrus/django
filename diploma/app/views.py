from django.shortcuts import render
from django.http import HttpResponseRedirect
from app.models import Article, Product, CartItem, Cart, Order
from django.contrib.auth.forms import UserCreationForm
from app.forms import CartForm, OrderForm, RegistrationForm,  SignupForm
from django.shortcuts import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout



def index(request):
    form = CartForm()
    articles = Article.objects.all().order_by('-date_pub')
    context = {
        'articles': articles,
        'form': form
    }
    return render(request, 'index.html', context)

def add_product_in_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    new_item, _ = CartItem.objects.get_or_create(product=product, item_total=product.price)

    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except DoesNotExist:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)

    if new_item not in cart.items.all():
        cart.items.add(new_item)
        cart.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        for cart_items in cart.items.all():
            if cart_items.product == product:
                cart_items.qty += 1
                cart_items.item_total += cart_items.item_total
                cart_items.save()
                return HttpResponseRedirect(reverse('index'))


def cart(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except DoesNotExist:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)

    template = 'cart.html'
    if request.method == 'POST':
        new_order = Order()
        new_order.user = request.user
        new_order.total = cart.cart_total
        new_order.save()
        for item in cart.items.all():
            cart.items.remove(item)
            cart.save()
        return render(request, template)

    new_cart_total = 0
    for item in cart.items.all():
        new_cart_total += item.item_total

    cart.cart_total = new_cart_total
    cart.save()
    context = {
        'cart': cart
    }
    return render(request, template, context)

def show_mobiles(request):
    template = 'smartphones.html'
    return render(request, template)

def show_product(request, id):
    template = 'phone.html'
    product = Product.objects.get(id=id)
    context = {
        'product': product
    }
    return render(request, template, context)

def login(request):
    form = SignupForm(request.POST)
    if form.is_valid():
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        username = User.objects.filter(email=email).first()
        user = authenticate(username=username.username, password=password)
        if user:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def sing_up(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save()
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        username = form.cleaned_data['username']
        new_user.username = username
        new_user.email = email
        new_user.set_password(password)
        new_user.save()
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('index'))
    context = {
        'form': form
    }
    return render(request, 'sing_up.html', context)

def empty(request):
    return render(request, 'empty_section.html')

def order_create(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except DoesNotExist:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    form = OrderForm(request.POST)
    if form.is_valid():
        new_order = Order()
        new_order.user = request.user
        new_order.save()
    context = {
        'form': form
    }
    return render(request, 'order.html', context)
