from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def get_all_post(request):
    
    return HttpResponse("<h1>Hello world</h1>")