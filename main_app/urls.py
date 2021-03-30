from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='index'),
 # Add this line below...
 path('about/', views.about, name='about')
]