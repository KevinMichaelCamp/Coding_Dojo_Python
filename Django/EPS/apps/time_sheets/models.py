from django.db import models
from decimal import Decimal

import bcrypt
import re

NAME_REGEX = re.compile(r'[a-zA-Z\s]+$')
EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def validate_login(self, postData):
        errors = {}

        if len(User.objects.filter(email = postData['email'])):
            user = User.objects.get(email = postData['email'])
            if bcrypt.checkpw(postData['password'].encode(), user.password):
                return errors
            else:
                errors['password'] = "Password incorrect"
                return errors

        else:
            errors['login'] = "Email not found in database"
            return errors

    def validate_reg(self, postData):
        errors = {}

        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters"
        elif not NAME_REGEX.match(postData['first_name']):
            errors['first_name'] = "First name must contain letters only"

        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"
        elif not NAME_REGEX.match(postData['last_name']):
            errors['last_name'] = "Last name must contain letters only"

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email format"
        elif len(User.objects.filter(email = postData['email'])):
            errors['email'] = "Email already exists in database"

        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        elif postData['password'] != postData['pw_confirm']:
            errors['password'] = "Password does not match password confirmation"

        return errors

class ShiftManager(models.Manager):
    def validate(self, postData):
        errors = {}

        if len(postData['description']) < 2:
            errors['description'] = "Description must be at least 2 characters"

        return errors

class QuoteManager(models.Manager):
    def validate_quote(self, postData):
        errors = {}

        if len(postData['author']) < 2:
            errors['author'] = "Author name must be at least 2 characters"

        if len(postData['quote']) == 0:
            errors['quote'] = "Quote field cannot be blank"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    user_level = models.SmallIntegerField(default=1)
    points_rate = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('7.25'))
    total_points = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    password = models.BinaryField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<User Object: {} {} {} {}".format(self.first_name, self.last_name, self.email, self.user_level)

    objects = UserManager()

class Shift(models.Model):
    clock_in = models.DateTimeField()
    clock_out = models.DateTimeField(null=True, blank=True)
    time_in = models.TimeField()
    time_out = models.TimeField(null=True, blank=True)
    date = models.DateField()
    description = models.TextField(null=True, blank=True)
    hours = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    points = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    employee = models.ForeignKey(User, related_name='shifts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Shift Object: {} {} {} {} {}".format(self.employee, self.clock_in, self.clock_out, self.date, self.points)

    objects = ShiftManager()

class Quote(models.Model):
    author = models.CharField(max_length=255)
    quote = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Quote object: {} {}".format(self.author, self.quote)

    objects = QuoteManager()
