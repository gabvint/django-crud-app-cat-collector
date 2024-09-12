from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Cat
from .forms import FeedingForm
# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    # success_url = '/cats/'


class CatUpdate(UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age']


class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def cat_index(request):
    cats = Cat.objects.all()  # returns a list of all cats
    return render(request, 'cats/index.html', {'cats': cats})


def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)  # return a specific cat object
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {
        'cat': cat,
        'feeding_form': feeding_form,
    })


def add_feeding(request, cat_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('cat-detail', cat_id=cat_id)
