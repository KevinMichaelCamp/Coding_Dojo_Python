from django.shortcuts import render
from ..login_register.models import User

def home(request):
    context = {
        'user': User.objects.get(id = request.session['id'])
    }

    return render(request, 'home.html', context)

def weather(request):
    pass
