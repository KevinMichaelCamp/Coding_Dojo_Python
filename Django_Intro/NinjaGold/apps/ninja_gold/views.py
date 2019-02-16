from django.shortcuts import render, redirect
from time import localtime, strftime
import random

# Create your views here.


def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0

    return render(request, 'index.html')


def process(request):
    if not 'messages' in request.session:
        request.session['messages'] = []

    if request.POST['button'] == 'farm':
        request.session['new_gold'] = random.randint(9, 20)
        request.session['gold'] += request.session['new_gold']
        request.session['messages'].append("Earned " + str(request.session['new_gold']) + " gold from the farm! - " + strftime(
            "%b-%d-%Y %H:%M %p", localtime()))

    if request.POST['button'] == 'cave':
        request.session['new_gold'] = random.randint(4, 10)
        request.session['gold'] += request.session['new_gold']
        request.session['messages'].append("Earned " + str(request.session['new_gold']) + " gold from the cave! - " + strftime(
            "%b-%d-%Y %H:%M %p", localtime()))

    if request.POST['button'] == 'house':
        request.session['new_gold'] = random.randint(1, 5)
        request.session['gold'] += request.session['new_gold']
        request.session['messages'].append("Earned " + str(request.session['new_gold']) +
                                           " gold from the house! - " + strftime("%b-%d-%Y %H:%M %p", localtime()))

    if request.POST['button'] == 'casino':
        request.session['new_gold'] = random.randint(-51, 50)
        request.session['gold'] += request.session['new_gold']
        request.session['messages'].append("Earned/Lost " + str(request.session['new_gold']) +
                                           " gold from the casino! - " + strftime("%b-%d-%Y %H:%M %p", localtime()))

    return redirect('/')


def clear(request):
    request.session.clear()
    return redirect('/')
