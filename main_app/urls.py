from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('products/', views.products_index, name='products'),
    path('products/calm/', views.calm, name='calm'),
    path('products/energize/', views.energize, name='energize'),
    path('products/indulge/', views.indulge, name='indulge'),
    path('products/romance/', views.romance, name='romance'),
    path('products/sleep/', views.sleep, name='sleep'),
    path('find_by_mood/', views.mood, name='view_by_mood'),
    
]