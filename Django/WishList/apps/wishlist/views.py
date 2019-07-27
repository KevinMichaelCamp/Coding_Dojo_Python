from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Item
import bcrypt


def add(request):
    errors = Item.objects.validate_item(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/create')
    else:
        Item.objects.create(
            item_name = request.POST['item_name'],
            added_by = User.objects.get(id=request.session['id'])
        )
        return redirect('/dashboard')


def addme(request, id):
    item = Item.objects.get(id=id)
    user = User.objects.get(id=request.session['id'])
    item.others.add(user)
    item.save()
    return redirect('/dashboard')

def create(request):
    context = {
        'user': User.objects.get(id=request.session['id'])
    }
    return render(request, 'create.html', context)


def dashboard(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        'others_items': Item.objects.exclude(added_by=user).exclude(others=user),
        'user': user,
        'user_items': Item.objects.filter(added_by=user),
        'user_other_items': Item.objects.filter(others=user)
    }
    return render(request, 'dashboard.html', context)


def delete(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect('/dashboard')


def display(request, id):
    context = {
        'item': Item.objects.get(id=id),
        'others': User.objects.filter(others_items=id),
        'user': User.objects.get(items=id)
    }
    return render(request, 'display.html', context)


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
            name =  request.POST['name'],
            username = request.POST['username'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()),
            hire_date = request.POST['hire_date']
        )
        request.session['id'] = user.id
        return redirect('/dashboard')


def remove(request, id):
    item = Item.objects.get(id=id)
    user = User.objects.get(id=request.session['id'])
    item.others.remove(user)
    item.save()
    return redirect('/dashboard')
