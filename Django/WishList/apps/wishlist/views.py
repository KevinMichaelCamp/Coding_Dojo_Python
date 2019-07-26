from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    context = {
        'user': User.objects.get(id=request.session['id'])
    }
    return render(request, 'dashboard.html', context)


def login(request):
    errors = User.objects.validate_login(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.get(username=request.POST['username'])
        request.session['id'] = user.id
        return redirect('/dashboard')


def logout(request):
    request.session.clear()
    return redirect('/')

    
def register(request):
    errors = User.objects.validate_register(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.create(
            name =  request.POST['name'],
            username = request.POST['username'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()),
            hire_date = request.POST['hire_date']
        )
        request.session['id'] = user.id
        return redirect('/dashboard')
