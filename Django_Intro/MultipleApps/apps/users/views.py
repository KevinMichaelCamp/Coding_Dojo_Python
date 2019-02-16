from django.shortcuts import render, HttpResponse

# Create your views here.

def register(request):
    return HttpResponse("Placeholder for users to create a new user record")

def login(request):
    return HttpResponse("Placeholder for users to login")

def users(request):
    return HttpResponse("Placeholder to later display all users")
