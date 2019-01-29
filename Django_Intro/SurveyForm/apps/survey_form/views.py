from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def process(request):
    if not 'count' in request.session:
        request.session['count'] = 0

    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        request.session['count'] += 1
        return redirect('/result')
    else:
        return redirect('/')

def result(request):
    context = {
        'name': request.session['name'],
        'location': request.session['location'],
        'language': request.session['language'],
        'comment': request.session['comment'],
        'count': request.session['count']
    }
    return render(request, 'result.html', context)

def reset(request):
    request.session.clear()
    return redirect('/')
