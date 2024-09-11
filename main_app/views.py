from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Cat


class CatCreate(CreateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cat_index(request):
    cats = Cat.objects.all() # returns a list of all cats
    return render(request, 'cats/index.html', {'cats': cats})

def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id) # return a specific cat object
    return render(request, 'cats/detail.html', {'cat': cat})