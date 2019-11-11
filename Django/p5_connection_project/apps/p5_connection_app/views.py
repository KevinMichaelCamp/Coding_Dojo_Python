from django.shortcuts import render, redirect
from .models import Blob

def index(request):
    context = {
        "blobs": Blob.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):
    Blob.objects.create(name=request.POST['name'], team=request.POST['team'])
    return redirect('/')
