from django.db import models
import bcrypt
import re

NAME_REGEX = re.compile(r'[a-zA-Z\s]+$')
EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA_Z0-9._-]+\.[a-zA-z]+$')

# Create your models here.

class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}

        if len(postData['name']) < 2:
            errors['name'] = "Name must be at least 2 characters long"
        if not NAME_REGEX.match(postData['name']):
            errors['name'] = "Name must only contain letters"

        if len(postData['alias']) < 2:
            errors['alias'] = "Alias must be at least 2 characters long"

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email format"
        elif len(User.objects.filter(email = postData['email'])):
            errors['email'] = "Email already exists in database"

        if len(postData['password']) < 8:
            errors['password'] = "Password word be at least 8 characters long"
        elif postData['password'] != postData['pw_confirm']:
            errors['password'] = "Password does not match confirmation"

        return errors

    def validate_login(self, postData):
        errors = {}

        if len(User.objects.filter(email = postData['email'])):
            user = User.objects.get(email = postData['email'])
            if bcrypt.checkpw(postData['password'].encode(), user.password):
                return errors
            else:
                errors['login'] = "Email/Password incorrect"
                return errors
        else:
            errors['login'] = "Email/Password incorrect"
            return errors

class BookManager(models.Manager):
    def validate_book(self, postData):
        errors = {}

        if len(postData['title']) == 0:
            errors['title'] = "Must enter book title"

        return errors

class User(models.Model):
    name = models.CharField(max_length=500)
    alias = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    password = models.BinaryField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<User object: {} {} {}".format(self.name, self.alias, self.email)

    objects = UserManager()

class Author(models.Model):
    author = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Author object: {}".format(self.author)

class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Book object: {} {} {}".format(self.title, self.author, self.rating)

    objects = BookManager()

class Review(models.Model):
    review = models.TextField()
    rating = models.SmallIntegerField(blank=True, null=True)
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Review object: {} {} {}".format(self.review, self.book, self.reviewer)
