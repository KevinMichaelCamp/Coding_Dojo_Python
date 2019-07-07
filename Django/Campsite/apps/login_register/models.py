from django.db import models
import bcrypt
import re

NAME_REGEX = re.compile(r'[a-zA-Z\s]+$')
EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.

class UserManager(models.Manager):
    def validate_login(self, postData):
        errors = {}

        if len(User.objects.filter(email = postData['email'])):
            user = User.objects.get(email= postData['email'])
            if bcrypt.checkpw(postData['password'].encode(), user.password):
                return errors
            else:
                errors['password'] = "Password incorrect"
                return errors
        else:
            errors['email'] = "Email not found in database"
            return errors


    def validate_register(self, postData):
        errors = {}

        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters"
        elif not NAME_REGEX.match(postData['first_name']):
            errors['first_name'] = "First name must contain only letters"

        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"
        elif not NAME_REGEX.match(postData['last_name']):
            errors['last_name'] = "Last name must contain only letters"

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email format"
        elif len(User.objects.filter(email = postData['email'])):
            errors['email'] = "Email already in database"

        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        elif postData['password'] != postData['pw_confirm']:
            errors['password'] = "Password does not match password confirmation"

        return errors



class User(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    user_level = models.SmallIntegerField(default=1)
    email = models.CharField(max_length=500)
    password = models.BinaryField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<User object: {} {} {} {}".format(self.first_name, self.last_name, self.user_level, self.email)

    objects = UserManager()
