from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from cart.cart import Cart



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

def ourpicks(request):
    products = Product.objects.all()
#    mochapick = none
#     for product in products:
    return render(request, 'ourpicks.html')

def mood(request):
    products = Product.objects.all()
    mood_no_repeat = []
    for product in products:

        mood_product = {
            "category": product.category,
            "img": product.catimg
        }
        # print(mood_product)
        # print(mood_product["category"])
        if mood_product["category"] not in mood_no_repeat:
            # print(product.category)
            mood_no_repeat.append(mood_product["category"])

            #inside of mood_no_repeat["category", add corresponding img]
           
           
            
    
    print(mood_no_repeat)

    return render(request, 'products/mood.html', {
        'products': mood_no_repeat,
        })

def mood_show(request, category):
    category = Product.objects.filter(category=category)
    # for category in category:
    print('********', category)
    
    return render(request, 'products/mood_show.html', {'category': category})

def cart(request):
    return render(request, 'ecommerce/cart.html')

def cart(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html')

def cart_checkout(request):
    cart = Cart(request)
    return render(request, 'cart/cart_checkout.html')

def cart_add(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return redirect('cart')

def item_clear(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.remove(product)
    return redirect("cart")

def item_increment(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return redirect("cart")

def item_decrement(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    for key,value in request.session['cart'].items():
        if value['quantity'] == 1:
            cart.remove(product)
            return redirect("cart")
        else:
            cart.decrement(product=product)
            return redirect("cart")

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")

def cart_detail(request):
    return render(request, 'cart/cart_detail.html')
    
def cart_total_amount(request):
	if request.user.is_authenticated:
		cart = Cart(request)
		total_bill = 0.0
		for key,value in request.session['cart'].items():
		    total_bill = total_bill + (float(value['price']) * value['quantity'])
		return {'cart_total_amount' : total_bill} 
	else:
		return {'cart_total_amount' : 0} 
