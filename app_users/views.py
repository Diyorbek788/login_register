# app_main/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def register_user(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(username=username, password=password)

        return redirect('login')
    else:
        return render(request, 'app_users/register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect('home')
        else:

            context = {'error': 'Foydalanuvchi ismi yoki parol notogri.'}
            return render(request, 'login.html', context)
    else:
        return render(request, 'app_users/login.html')


def home_page(requests):
    return render(requests, 'app_main/home.html')
