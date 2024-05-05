# project/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .views import login_user

urlpatterns = [

    path('register/', views.register_user, name='register'),

    path('login/', views.login_user, name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('home/', views.home_page, name='home'),

]