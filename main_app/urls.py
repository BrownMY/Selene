from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.about, name='about'),
    path('signup/', views.about, name='sign_up'),
    path('products/', views.about, name='products'),
    path('products/calm/', views.about, name='about'),
    path('products/energize/', views.about, name='about'),
    path('products/indulge/', views.about, name='about'),
    path('products/romance/', views.about, name='about'),
    path('products/sleep/', views.about, name='about'),
    path('products/find_by_mood/', views.about, name='about'),
    
]