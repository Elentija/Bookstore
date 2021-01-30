from django.shortcuts import render
from MyLibrary.models import Client


def home(request):
    return render(request, 'home/home.html')
