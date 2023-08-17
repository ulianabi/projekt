from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement

def index(requset):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(requset, 'index.html', context)

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
