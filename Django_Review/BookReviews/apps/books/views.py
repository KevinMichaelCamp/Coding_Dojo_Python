from django.shortcuts import render, redirect
from django.contrib import messages
from ..login_register.models import User
from .models import Author, Book, Review

def books(request):
    context = {
        'books': Book.objects.all(),
        'reviews': Review.objects.order_by('-created_at')[:3],
        'user': User.objects.get(id=request.session['id'])
    }
    return render(request, 'books.html', context)

def add(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'add.html', context)

def create(request):
    errors = Book.objects.validate_book(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/add')
    else:
        if len(request.POST['author']):
            author = Author.objects.create(author = request.POST['author'])
        else:
            author = Author.objects.get(id=request.POST['author_id'])

        book = Book.objects.create(
            title = request.POST['title'],
            author = author
        )

        Review.objects.create(
            review = request.POST['review'],
            rating = request.POST['rating'],
            book = book,
            reviewer = User.objects.get(id=request.session['id'])
        )

        messages.success(request, "New book and review added")
        return redirect('/books')

def display(request, id):
    book = Book.objects.get(id=id)
    context = {
        'book': book,
        'reviews': Review.objects.filter(book=book),
        'user': User.objects.get(id=request.session['id'])
    }
    return render(request, 'display.html', context)

def review(request, id):
    book = Book.objects.get(id=id)
    Review.objects.create(
        review = request.POST['review'],
        rating = request.POST['rating'],
        book = book,
        reviewer = User.objects.get(id=request.session['id'])
    )
    return redirect('/books')

def user(request, id):
    user = User.objects.get(id=id)
    context = {
        'count': Review.objects.filter(reviewer=user).count(),
        'reviews': Review.objects.filter(reviewer=user),
        'user': user,
    }
    return render(request, 'user.html', context)

def delete(request, id):
    review = Review.objects.get(id=id)
    review.delete()
    return redirect('/books')
