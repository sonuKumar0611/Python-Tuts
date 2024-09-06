from django.urls import path
from . import views
from . import authvw


urlpatterns=[
    path('', views.show_my_shop , name="my_shop"),
    path('login', authvw.Login, name='login'), 
    path('logout', authvw.logout, name='logout'), 
    path('store', views.show_my_shop, name='store'), 
    path('signup', views.show_my_shop, name='signup'), 
    path('login', views.show_my_shop, name='login'), 
    path('logout', views.show_my_shop, name='logout'), 
    path('cart/', views.cart_view, name='cart'),
    path('update-cart/', views.update_cart, name='update_cart'), 
    path('check-out', views.show_my_shop, name='checkout'), 
    path('orders', views.show_my_shop, name='orders'), 
  
]