from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.

def index(request):
    context = {'courses': Course.objects.all()}
    return render(request, 'index.html', context)

def create(request):
    errors = Course.objects.validate(request.POST)
    errors2 = Description.objects.validate(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    elif len(errors2):
        for key, value in errors2.items():
            messages.error(request, value)
        return redirect('/')

    else:
        Course.objects.create(name = request.POST['name'])
        course = Course.objects.last()
        Description.objects.create(desc = request.POST['desc'], course = course)
        return redirect('/')

def confirm(request, id):
    context = {'course': Course.objects.get(id=id)}
    return render(request, 'confirm.html', context)

def delete(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/')
