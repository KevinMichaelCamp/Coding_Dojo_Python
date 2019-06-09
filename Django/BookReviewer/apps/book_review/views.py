from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User
from .models import Author
from .models import Book
from .models import Review

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.validate(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    else:
        user = User.objects.create(
            name = request.POST['name'],
            alias = request.POST['alias'],
            email = request.POST['email'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            )
        messages.success(request, "New user registered")
        request.session['id'] = user.id
        return redirect('/books')

def login(request):
    errors = User.objects.validate_login(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    else:
        user = User.objects.get(email = request.POST['email'])
        request.session['id'] = user.id
        return redirect('/books')

def library(request):
    context = {'users': User.objects.all(), 'books': Book.objects.all()}
    return render(request, 'users.html', context)

def books(request):
    context = {
        'user': User.objects.get(id = request.session['id']),
        'reviews': Review.objects.order_by('-created_at')[:3],
        'books': Book.objects.all()
    }
    return render(request, 'books.html', context)

def new_book(request):
    context = {'authors': Author.objects.all()}
    return render(request, 'add_books.html', context)

def add(request):
    errors = Book.objects.validate_book(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.errors(request, value)
        return redirect('/books')

    else:
        if len(request.POST['author']):
            author = Author.objects.create(author = request.POST['author'])
        else:
            author = Author.objects.get(id = request.POST['author_id'])

        book = Book.objects.create(
            title = request.POST['title'],
            author = author,
        )

        # Create Stars
        stars = ""
        if request.POST['rating'] == 0:
            stars = "&#x2606;&#x2606;&#x2606;&#x2606;&#x2606;"
        elif request.POST['rating'] == 1:
            stars = "&#x2605;&#x2606;&#x2606;&#x2606;&#x2606;"
        elif request.POST['rating'] == 2:
            stars = "&#x2605;&#x2605;&#x2606;&#x2606;&#x2606;"
        elif request.POST['rating'] == 3:
            stars = "&#x2605;&#x2605;&#x2605;&#x2606;&#x2606;"
        elif request.POST['rating'] == 4:
            stars = "&#x2605;&#x2605;&#x2605;&#x2605;&#x2606;"
        else:
            stars = "&#x2605;&#x2605;&#x2605;&#x2605;&#x2605;"

        Review.objects.create(
            review = request.POST['review'],
            rating = request.POST['rating'],
            stars = stars,
            book = book,
            reviewer = User.objects.get(id = request.session['id'])
        )

        messages.success(request, "New book and review added")
        return redirect('/books')

def add_review(request):
    Review.objects.create(
        review = request.POST['review'],
        rating = request.POST['rating'],
        book = Book.objects.get(id = request.POST['book_id']),
        reviewer = User.objects.get(id = request.session['id'])
    )
    return redirect('/books')

def display(request, id):
    book = Book.objects.get(id = id)
    context = {
        'book': book,
        'reviews': Review.objects.filter(book = book)
    }
    return render(request, 'display.html', context)

def user_reviews(request, id):
    user = User.objects.get(id = id)
    context = {
        'user': user,
        'reviews': Review.objects.filter(reviewer = user),
        'count': Review.objects.filter(reviewer = user).count()
    }
    return render(request, 'user_reviews.html', context)

def home(request):
    return redirect('/books')

def logout(request):
    request.session.clear()
    return redirect('/')
