from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
from datetime import datetime
from decimal import Decimal
from pytz import timezone
from dateutil import tz
import pytz
import bcrypt
from .models import User
from .models import Shift

def index(request):
    return render(request, 'index.html')

def validate_login(request):
    errors = User.objects.validate_login(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    else:
        user = User.objects.get(email = request.POST['email'])
        request.session['id'] = user.id
        return redirect('/home')

def validate_reg(request):
    errors = User.objects.validate_reg(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    else:
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            user_level = 1,
            total_points = 0,
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        )

        if len(User.objects.all()) == 1:
            user.user_level = 9
            user.save()
            messages.success(request, "New Admin Added")
            request.session['id'] = user.id
            return redirect('/home')

        else:
            messages.success(request, "New User Added")
            request.session['id'] = user.id
            return redirect('/home')

def home(request):
    now = datetime.now(timezone('MST'))
    print(now)

    user = User.objects.get(id=request.session['id'])
    user_shifts = Shift.objects.filter(employee = user)

    # Calculate & save user total points
    if user_shifts[0].clock_out != None:
        calc_points = User.objects.annotate(sum_points = Sum('shifts__points')).get(id=request.session['id'])
        total_points = calc_points.sum_points
        user.total_points = round(total_points, 2)
        user.save()

    # Calculate & save company total points
    calc_points = User.objects.all().aggregate(all_points = Sum('total_points'))
    company_points = round(calc_points['all_points'], 2)

    context = {
        'company_points': company_points,
        'date_time': now.strftime('%I:%M %p | %d %B %Y'),
        'shifts': Shift.objects.all(),
        'user': user,
        'user_shifts': Shift.objects.filter(employee=user),
        'users': User.objects.all()
    }

    return render(request, 'home.html', context)

def points(request):
    now = datetime.now(timezone('MST'))

    user = User.objects.get(id=request.session['id'])
    user_shifts = Shift.objects.filter(employee = user)

    # Calculate & save user total points
    if user_shifts[0].clock_out != None:
        calc_points = User.objects.annotate(sum_points = Sum('shifts__points')).get(id=request.session['id'])
        total_points = calc_points.sum_points
        user.total_points = round(total_points, 2)
        user.save()

    # Calculate & save company total points
    calc_points = User.objects.all().aggregate(all_points = Sum('total_points'))
    company_points = round(calc_points['all_points'], 2)

    context = {
        'company_points': company_points,
        'date_time': now.strftime('%I:%M %p | %d %B %Y'),
        'shifts': Shift.objects.all(),
        'user': User.objects.get(id=request.session['id']),
        'user_shifts': Shift.objects.filter(employee=user),
        'users': User.objects.all()
    }
    return render(request, 'points.html', context)

def report(request):
    return render(request, 'report.html')

def settings(request):
    return render(request, 'settings.html')

def admin_home(request):
    return render(request, 'admin_home.html')

def clock_in(request):
    shift = Shift.objects.create(
        clock_in = datetime.now(timezone('MST')),
        time_in = datetime.now(timezone('MST')),
        date = datetime.now(timezone('MST')),
        employee = User.objects.get(id = request.session['id'])
    )

    request.session['shift_id'] = shift.id
    return redirect('/clocked_in')

def clock_out(request):
    errors = Shift.objects.validate(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/clocked_in')

    else:
        user = User.objects.get(id = request.session['id'])
        shift = Shift.objects.get(id = request.session['shift_id'])

        # Calculate work hours & points (use rate!!!)
        timeDiff = datetime.now(timezone('MST')) - shift.clock_in
        total_seconds = int(timeDiff.total_seconds())
        hours = Decimal(total_seconds/3600)
        points = hours * user.points_rate

        print("total_seconds" + str(total_seconds), 'hours' + str(hours), "points" + str(points))
        shift.clock_out = datetime.now(timezone('MST'))
        shift.time_out = datetime.now(timezone('MST'))
        shift.hours = hours
        shift.points = points
        shift.description = request.POST['description']
        shift.save()
        # Add shift points to total points
        user.total_points += points
        user.save()

    return redirect('/home')

def clocked_in(request):
    now = datetime.now(timezone('MST'))

    user = User.objects.get(id=request.session['id'])
    user_shifts = Shift.objects.filter(employee = user)
    print(user_shifts)

    # Calculate & save user total points
    if user_shifts[0].clock_out != None:
        calc_points = User.objects.annotate(sum_points = Sum('shifts__points')).get(id=request.session['id'])
        total_points = calc_points.sum_points
        user.total_points = round(total_points, 2)
        user.save()

    # Calculate & save company total points
    calc_points = User.objects.all().aggregate(all_points = Sum('total_points'))
    company_points = round(calc_points['all_points'], 2)

    context = {
        'company_points': company_points,
        'date_time': now.strftime('%I:%M %p | %d %B %Y'),
        'shifts': Shift.objects.all(),
        'user': user,
        'users': User.objects.all()
    }

    return render(request, 'clocked_in.html', context)

def forgot(request):
    #HELP
    now = datetime.now(timezone('MST'))

    user = User.objects.get(id=request.session['id'])
    shift = Shift.objects.get(id=request.POST['shift_id'])

    naive = datetime.strptime (request.POST['clock_out']+':00', "%Y-%m-%dT%H:%M:%S")
    aware = pytz.utc.localize(naive)
    tzlocal = aware.astimezone(tz.tzlocal())

    print(aware)
    print(tzlocal)
    print(request.POST['clock_out'])
    print(shift.clock_in)
    # Calculate work hours & points (use rate!!!)
    timeDiff = tzlocal - shift.clock_in
    total_seconds = int(timeDiff.total_seconds())
    hours = Decimal(total_seconds/3600)
    points = hours * user.points_rate

    print("total_seconds" + str(total_seconds), 'hours' + str(hours), "points" + str(points))
    shift.clock_out = tzlocal
    shift.time_out = tzlocal
    shift.hours = hours
    shift.points = points
    shift.description = request.POST['description']
    shift.save()
    # Add shift points to total points
    user.total_points += points
    user.save()


    print(request.POST)
    return redirect('/home')

def logout(request):
    request.session.clear()
    return redirect('/')
