from django.shortcuts import redirect, render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Placeholder to later display list of blogs.")

def new(request):
    return HttpResponse("Placeholder to display a new form to create a blog.")

def create(request):
    return redirect('blogs')

def show(request, number):
    return HttpResponse("Placeholder to display blog " + number)

def edit(request, number):
    return HttpResponse("Placeholder to edit blog " + number)

def delete(request, number):
    return HttpResponse("Placeholder to delete blog " + number)
