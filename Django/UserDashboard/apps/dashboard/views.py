from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import bcrypt
from .models import User
from .models import Message

# Create your views here.

def index(request):
    return render(request, 'index.html')

def signin(request):
    return render(request, 'signin.html')

def login(request):
    errors = User.objects.validate_login(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/signin')

    else:
        user = User.objects.filter(email=request.POST['email'])
        request.session['id'] = user[0].id
        if user[0].user_level == 9:
            return redirect('/admin_dashboard')
        else:
            return redirect('/user_dashboard')

def registration(request):
    return render(request, 'registration.html')

def register(request):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/registration')

    else:
        User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            user_level = 1,
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        )
        if len(User.objects.all()) == 1:
            admin = User.objects.get(id=1)
            admin.user_level = 9
            admin.save()
            user = User.objects.filter(email=request.POST['email'])
            request.session['id'] = user[0].id
            messages.success(request, "Admin Registered")
            return redirect('/admin_dashboard')
        else:
            user = User.objects.filter(email=request.POST['email'])
            request.session['id'] = user[0].id
            messages.success(request, "New User Registered")
            return redirect('/user_dashboard')

def admin_dashboard(request):
    context = {'users': User.objects.all()}
    return render(request, 'admin_dashboard.html', context)

def user_dashboard(request):
    user = User.objects.get(id = request.session['id'])
    if user.user_level == 9:
        return redirect('/admin_dashboard')
    else:
        context = {'users': User.objects.all()}
        return render(request, 'user_dashboard.html', context)

def add(request):
    return render(request, 'add_user.html')

def admin_add(request):
    errors = User.objects.validate(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/add')

    else:
        User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            user_level = 1,
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        )
        messages.success(request, "New User Registered")
        return redirect('/admin_dashboard')

def user_edit(request):
    return render(request, 'user_edit.html')

def admin_edit(request, id):
    context = {'id': id}
    return render(request, 'admin_edit.html', context)

def admin_edit_info(request, id):
    errors = User.objects.validate_info(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/admin_edit/'+ id)

    else:
        user = User.objects.get(id = id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.user_level = request.POST['user_level']
        user.save()
        return redirect('/admin_dashboard')

def admin_edit_password(request, id):
    errors = User.objects.validate_password(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/admin_edit/' + id)

    else:
        user = User.objects.get(id = id)
        user.password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user.save()
        return redirect('/admin_dashboard')

def edit_info(request):
    errors = User.objects.validate_info(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/user_edit')

    else:
        user = User.objects.get(id = request.session['id'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('/user_dashboard')

def edit_password(request):
    errors = User.objects.validate_password(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/user_edit')

    else:
        user = User.objects.get(id = request.session['id'])
        user.password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user.save()
        return redirect('/user_dashboard')


def delete(request, id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect('/admin_dashboard')

def show(request, id):
    user = User.objects.get(id = id)
    context = {'user': User.objects.get(id = id),
                'messages': user.messages_recieved.all()}
    return render(request, 'user_info.html', context)

def message(request, id):
    user = User.objects.get(id=id)
    Message.objects.create(
        message = request.POST['message'],
        recipient = User.objects.get(id=id),
        sender = User.objects.get(id = request.POST['sender'])
    )
    print(Message.objects.all())
    return redirect('/show/' + id)

def logout(request):
    request.session.clear()
    return redirect('/')
