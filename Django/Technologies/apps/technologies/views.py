from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Technology


def index(request):
    techs = Technology.objects.all()
    context = {
        'technologies': techs
    }
    return render(request, 'index.html', context)


def new(request):
    return render(request, 'new.html')


def create(request):
    errors = Technology.objects.validate(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/new')

    else:
        tech = Technology.objects.create(
            name=request.POST['name'],
            tech_type=request.POST['tech_type'],
            purpose=request.POST['purpose'],
            release_date=request.POST['release_date'],
            imgurl=request.POST['imgurl']
        )
        tech.save()
        messages.success(request, "New Tech Added")
        return redirect('/')


def show(request, id):
    tech = Technology.objects.get(id=id)
    context = {
        'tech': tech
    }
    return render(request, "show.html", context)


def edit(request, id):
    tech = Technology.objects.get(id=id)
    context = {
        'tech': tech
    }
    return render(request, "edit.html", context)


def update(request, id):
    tech = Technology.objects.get(id=id)
    tech.name = request.POST['name']
    tech.tech_type = request.POST['tech_type']
    tech.purpose = request.POST['purpose']
    tech.release_date = request.POST['release_date']
    tech.imgurl = request.POST['imgurl']
    tech.save()
    messages.success(request, "Tech Info Edited")
    return redirect('/edit/' + id)


def delete(request, id):
    Technology.objects.get(id=id).delete()
    return redirect('/')
