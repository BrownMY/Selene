from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def sign_up(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # ok user created log them in
            login(request, user)
            return redirect('index')
        else:
            error_message = 'That was a no go. Invalid signup'
    # this will run after if it's not a POST or it was invalid
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form,
        'error_message': error_message
    })

def log_in(request):
    return render(request, 'login.html')

def products_index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})

def products_show(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'products/show.html', {'product': product})

def spotlight(request):
    products = Product.objects.all()
    return render(request, 'products/spotlight.html', {'products': products})

def mood(request):
    products = Product.objects.all()
    mood_no_repeat = []
    for product in products:
        if product.category not in mood_no_repeat:
            mood_no_repeat.append(product.category)
    
    return render(request, 'products/mood.html', {'products': mood_no_repeat})

def mood_show(request, category):
    category = Product.objects.filter(category=category)
    # for category in category:
    print('********', category)
    
    return render(request, 'products/mood_show.html', {'category': category})

def cart(request):
    return render(request, 'ecommerce/cart.html')


# def calm(request):
#     products = Product.objects.all()
#     return render(request, 'products/calm.html', {'products': products})

# def energize(request):
#     return render(request, 'products/energize.html')

# def indulge(request):
#     return render(request, 'products/indulge.html')


# def romance(request):
#     return render(request, 'products/romance.html')


# def sleep(request):
#     return render(request, 'products/sleep.html')

