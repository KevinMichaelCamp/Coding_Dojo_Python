from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User
from .models import Race
from .models import Character

# Create your views here.
def create(request):
    #Set race default attributes

    char = Character.objects.create(
        name = request.POST['name'],
        sex = request.POST['sex'],
        race = request.POST['race']
        )

def existing(request):
    context = {
        'user': User.objects.get(id=request.session['id'])
    }

    return render(request, 'existing.html', context)

def home(request):
    context = {
        'user': User.objects.get(id=request.session['id'])
    }

    return render(request, 'home.html', context)

def index(request):
    return render(request, 'index.html')

def login(request):
    pass

def logout(request):
    request.session.clear()
    return redirect('/')

def new(request):
    context = {
        'user': User.objects.get(id=request.session['id'])
    }
    return render(request, 'new.html', context)

def register(request):
    errors = User.objects.validate_reg(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    else:
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            )

        messages.success(request, "New User Added")
        request.session['id'] = user.id
        return redirect('/home')
