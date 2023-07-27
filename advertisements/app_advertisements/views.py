from django.shortcuts import render
from django.http import HttpResponse

def index(requset):
    return render(requset, 'index.html')

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(requset):
    return render(requset, 'advertisement-post.html')
def register(requset):
    return render(requset, 'register.html')
def login(requset):
    return render(requset, 'login.html')
def profile(requset):
    return render(requset, 'profile.html')