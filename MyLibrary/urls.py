from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/new/', views.book_new, name='book_new'),
    path('book/<int:pk>', views.book_details, name='book_details'),

    path('cart/<int:pk>', views.add_to_cart, name='add_to_cart'),
    path('cart_all', views.cart_all, name='cart_all'),
    path('cart/delete/<int:pk>', views.book_remove, name='book_remove'),

    path('client/new/', views.client_new, name='client_new'),
    path('client/<int:pk>', views.client_details, name='client_details'),
    path('client/login/', views.client_login, name='client_login'),
    path('client/reqister', views.client_register, name='client_register'),
    path('client/logout', views.client_logout, name='client_logout'),

    path('order/address/', views.order_set_address, name='order_address'),
    path('order/delivery/<int:pk>', views.order_set_delivery, name='order_delivery'),
    path('order/submit_order', views.submit_order, name='submit_order'),
    path('order/summary/<int:pk>', views.order_summary, name='order_summary'),

    path('home', views.home, name='home'),
    ]