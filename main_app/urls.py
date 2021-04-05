from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('signup/', views.sign_up, name='sign_up'),
    path('products/', views.products_index, name='products_index'),  
    path('products/spotlight/', views.spotlight, name='spotlight'),  
    path('products/<int:product_id>/', views.products_show, name='products_show'),
    path('products/mood/', views.mood, name='mood'),
    path('products/mood/<str:category>', views.mood_show, name='mood_show'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:product_id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:product_id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:product_id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail, name='cart_detail'),
    path('ourpicks/', views.ourpicks, name='ourpicks'),
    path('cart_checkout', views.cart_checkout, name='cart_checkout')
]