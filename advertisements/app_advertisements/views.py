from django.shortcuts import render
from django.http import HttpResponse

def index(requset):
    return render(requset, 'index.html')
def top_sellers()
