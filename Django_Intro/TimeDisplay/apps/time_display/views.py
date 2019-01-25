from django.shortcuts import render, redirect
from datetime import datetime

def index(request):
    now = datetime.now()
    context = {
        'time': datetime.strftime(now, "%H:%M %p %m-%d-%Y")
    }
    return render(request, 'index.html', context)
