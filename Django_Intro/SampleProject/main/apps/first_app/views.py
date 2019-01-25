from django.shortcuts import render, HttpResponse, redirect


def index(request):
    context = {
        'first_name': "Kevin",
        'last_name': "Camp",
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        print("*" * 50)
        print(request.POST['name'])
        print(request.POST['desc'])
    return redirect('/')
