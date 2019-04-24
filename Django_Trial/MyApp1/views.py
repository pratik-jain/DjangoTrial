from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Djangooooo!")

# Create your views here.
