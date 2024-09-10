from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
    return render(request, 'about.html')