from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User, Friendship


def index(request):
    return render(request, 'index.html')


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
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        )
        request.session['id'] = user.id
        messages.success(request, "New User Created")
        return redirect('/home')


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


def logout(request):
    request.session.clear()
    return redirect('/')


def home(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        'current_user': user,
        'curr_users_friends': user.friends.all(),
        'friendships': Friendship.objects.all(),
        'users': User.objects.all()
    }
    print(user.friends.all())
    return render(request, 'home.html', context)

def friend(request, id):
    user = User.objects.get(id=request.session['id'])
    friend = User.objects.get(id=id)
    Friendship.objects.create(
        friend = friend,
        friended_by = user
    )
    return redirect('/home')

def unfriend(request, id):
    user = User.objects.get(id=request.session['id'])
    friend = User.objects.get(id=id)
    friendship = Friendship.objects.get(friend=friend, friended_by=user)
    friendship.delete()
    return redirect('/home')
