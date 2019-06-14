from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('locations', views.locations, name='locations'),
    path('menu', views.menu, name='menu'),
    path('onlineShopping', views.onlineShopping, name='onlineShopping'),
    path('offers', views.offers, name='offers'),
    path('contactUs', views.contactUs, name='contactUs'),
    path('signup', views.signup, name='signup'),
    path('login', views.signin, name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]