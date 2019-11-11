from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def python(request):
    return render(request, 'python.html')

def ruby(request):
    pass

def mean(request):
    pass
