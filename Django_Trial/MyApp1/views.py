from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Djangoooooa!")

# Create your views here.
