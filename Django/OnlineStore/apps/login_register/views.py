from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User


def index(request):
    return render(request, 'index.html')


def login(request):
    errors = User.objects.validate_login(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['id'] = user.id
        return redirect('/home')


def register(request):
    errors = User.objects.validate_register(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    else:
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            user_level = 1,
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        )
        request.session['id'] = user.id

        if len(User.objects.all()) == 1:
            user.user_level = 9
            user.save()
            messages.success(request, "New Admin Added")
            return redirect('/home')

        else:
            messages.success(request, "New User Added")
            return redirect('/home')
