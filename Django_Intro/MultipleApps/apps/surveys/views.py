from django.shortcuts import render, HttpResponse

# Create your views here.

def surveys(request):
    return HttpResponse("Placeholder to display all the surveys created")

def new(request):
    return HttpResponse("Placeholder for users to add a new survey")
