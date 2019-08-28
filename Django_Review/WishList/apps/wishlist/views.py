from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User, Item

def index(request):
    return render(request, 'index.html')


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
            name = request.POST['name'],
            username = request.POST['username'],
            hire_date = request.POST['hire_date'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        )
        request.session['id'] = user.id
        messages.success(request, "New User Created")
        return redirect('/dashboard')


def dashboard(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        'other_items': Item.objects.exclude(added_by=user).exclude(wished_by=user),
        'user': user,
        'user_items': Item.objects.filter(added_by=user),
        'user_other_items': Item.objects.filter(wished_by=user)
    }
    return render(request, 'dashboard.html', context)


def add(request):
    return render(request, 'add.html')


def create(request):
    user = User.objects.get(id=request.session['id'])
    errors = Item.objects.validate_item(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/new')
    else:
        Item.objects.create(
            name = request.POST['name'],
            added_by = user,
        )
        messages.success(request, "New Item Created")
        return redirect('/dashboard')
