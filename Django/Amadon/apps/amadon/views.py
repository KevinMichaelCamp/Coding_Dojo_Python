from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

def buy(request):
    request.session['total'] = 0
    if not 'grand_total' in request.session:
        request.session['grand_total'] = 0
    if not 'items' in request.session:
        request.session['items'] = 0

    if int(request.POST['shirt']) > 0:
        request.session['total'] = 19.99 * int(request.POST['shirt'])
        request.session['items'] += int(request.POST['shirt'])
        return redirect('/checkout')

    elif int(request.POST['sweatshirt']) > 0:
        request.session['total'] = 29.99 * int(request.POST['sweatshirt'])
        request.session['items'] += int(request.POST['sweatshirt'])
        return redirect('/checkout')

    elif int(request.POST['mug']) > 0:
        request.session['total'] = 4.99 * int(request.POST['mug'])
        request.session['items'] += int(request.POST['mug'])
        return redirect('/checkout')

    elif int(request.POST['book']) > 0:
        request.session['total'] = 49.99 * int(request.POST['book'])
        request.session['items'] += int(request.POST['book'])
        return redirect('/checkout')

    else:
        return redirect('/')

def checkout(request):
    request.session['grand_total'] += request.session['total']
    context = {'grand_total': round(request.session['grand_total'], 2), 'total': request.session['total'], 'items': request.session['items']}
    return render(request, 'checkout.html', context)

def clear(request):
    request.session.clear()
    return redirect('/')
