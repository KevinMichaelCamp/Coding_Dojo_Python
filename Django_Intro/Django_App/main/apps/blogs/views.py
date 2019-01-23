from django.shortcuts import render, HttpResponse, redirect

#VIEWS
def index(request):
    response = "Placeholder to later DISPLAY LIST of blogs"
    return HttpResponse(response)

def new(request):
    response = "Placeholder to DISPLAY A NEW FORM to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, number):
    response = "Placeholder to DISPLAY blog number " + number
    return HttpResponse(response)

def edit(request, number):
    response = "Placeholder to EDIT blog number " + number
    return HttpResponse(response)

def destroy(request, number):
    return redirect('/')
