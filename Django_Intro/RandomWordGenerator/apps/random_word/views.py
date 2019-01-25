from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


def index(request):
    if not 'count' in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    context = {
        'count': request.session['count'],
        'word': get_random_string(length=14)
    }
    return render(request, 'index.html', context)


def reset(request):
    request.session.clear()
    return redirect('/')
