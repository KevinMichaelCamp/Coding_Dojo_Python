from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.

def index(request):
    context = {'users': User.objects.all()}
    return render(request, 'index.html', context)

def create(request):
    return render(request, 'create.html')

def validate(request):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('create')

    else:
        user = User.objects.create()
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        messages.success(request, "User Successfully Created")
        return redirect('/')

def revalidate(request, id):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/edit/'+id)

    else:
        user = User.objects.get(id=id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        messages.success(request, "User Successfully Edited")
        return redirect('/')


def show(request, id):
    context = {'user': User.objects.get(id=id)}
    return render(request, 'show.html', context)

def edit(request, id):
    context = {'user': User.objects.get(id=id)}
    return render(request, 'edit.html', context)


def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')
