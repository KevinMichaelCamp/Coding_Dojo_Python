from django.db import models
from ..login_register.models import User

class BookManager(models.Manager):
    def validate_book(self, postData):
        errors = {}

        if len(postData['title']) < 2:
            errors['title'] = "Title must be at least 2 charaters"

        return errors


class Author(models.Model):
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Author object: {}".format(self.author)


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Book object: {} {}".format(self.title, self.author)

    objects = BookManager()


class Review(models.Model):
    review = models.TextField(blank=True, null=True)
    rating = models.SmallIntegerField(blank=True, null=True)
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Review object: {} {} {} {}".format(self.book, self.reviewer, self.review, self.rating)
