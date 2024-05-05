from django.shortcuts import render


def home_page(requests):
    return render(requests, 'app_main/home.html')

# Create your views here.
