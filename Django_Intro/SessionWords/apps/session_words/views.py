from django.shortcuts import render, redirect
from time import localtime, strftime


def index(request):
    return render(request, 'index.html')


def create(request):
    if not 'words' in request.session:
        request.session['words'] = []

    if 'size' in request.POST:
        font = '200%'
    else:
        font = '100%'

    if 'color' in request.POST:
        color = request.POST['color']
    else:
        color = 'black'

    all_words = request.session['words']
    if request.method == 'POST':
        all_words.append({'word': request.POST['words'], 'color': color, 'font': font, 'time': strftime(
            "%b-%d-%Y %H:%M %p", localtime())})

    print(all_words)
    request.session['words'] = all_words
    return redirect('/')


def clear(request):
    request.session.clear()
    return redirect('/')
