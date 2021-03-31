from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


# def sign_up(request):
#     error_message = ''
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # ok user created log them in
#             login(request, user)
#             return redirect('index')
#         else:
#             error_message = 'That was a no go. Invalid signup'
#     # this will run after if it's not a POST or it was invalid
#             form = UserCreationForm()
#         return render(request, 'registration/signup.html', {
#             'form': form,
#             'error_message': error_message
#         })

def login(request):
    return render(request, 'login.html')

def products_index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})

def calm(request):
    return render(request, 'products/calm.html')

def energize(request):
    return render(request, 'products/energize.html')

def indulge(request):
    return render(request, 'products/indulge.html')

def romance(request):
    return render(request, 'products/romance.html')

def sleep(request):
    return render(request, 'products/sleep.html')

def mood(request):
    return render(request, 'products/mood.html')



