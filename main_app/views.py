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
