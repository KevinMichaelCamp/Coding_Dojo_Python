from django.db import models
import bcrypt
import re

NAME_REGEX = re.compile(r'[a-zA-Z\s]+$')
EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA_Z0-9._-]+\.[a-zA-z]+$')


class UserManager(models.Manager):
    def validate_login(self, postData):
        errors = {}

        if len(User.objects.filter(email=postData['email'])):
            user = User.objects.get(email=postData['email'])
            if bcrypt.checkpw(postData['password'].encode(), user.password):
                return errors
            else:
                errors['login'] = "Email/password incorrect"
                return errors
        else:
            errors['login'] = "Email/password incorrect"
            return errors

        return errors

    def validate_register(self, postData):
        errors = {}

        if len(postData['name']) < 2:
            errors['name'] = "Name must be at least 2 characters"
        elif not NAME_REGEX.match(postData['name']):
            errors['name'] = "Name must only contain letters"

        if len(postData['alias']) < 2:
            errors['alias'] = "Alias must be at least 2 characters"

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email format"
        elif len(User.objects.filter(email=postData['email'])):
            errors['email'] = "Email already in use"

        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        if postData['password'] != postData['pw_confirm']:
            errors['pw_confirm'] = "Passwords must match"

        return errors


class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.BinaryField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<User object: {} {} {}".format(self.name, self.alias, self.email)

    objects = UserManager()
