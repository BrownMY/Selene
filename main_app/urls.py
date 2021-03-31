from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.about, name='about'),
    path('signup/', views.about, name='about'),
    path('index/', views.about, name='about'),
    path('calm/', views.about, name='about'),
    path('energize/', views.about, name='about'),
    path('indulge/', views.about, name='about'),
    path('romance/', views.about, name='about'),
    path('sleep/', views.about, name='about'),
    path('mood/', views.about, name='about'),
    
]