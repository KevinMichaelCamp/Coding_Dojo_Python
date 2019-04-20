from django.db import models
import bcrypt
import re

NAME_REGEX = re.compile(r'[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA_Z0-9._-]+\.[a-zA-z]+$')

# Create your models here.
class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}

        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters"
        if not NAME_REGEX.match(postData['first_name']):
            errors['first_name'] = "First name must only contain lettters"

        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"
        if not NAME_REGEX.match(postData['last_name']):
            errors['last_name'] = "Last name must only contain lettters"

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address format"
        elif len(User.objects.filter(email = postData['email'])):
            errors['email'] = "Email already exists in database"

        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"

        if postData['password'] != postData['pw_confirm']:
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

    def validate_info(self, postData):
        errors = {}

        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters"
        if not NAME_REGEX.match(postData['first_name']):
            errors['first_name'] = "First name must only contain lettters"

        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"
        if not NAME_REGEX.match(postData['last_name']):
            errors['last_name'] = "Last name must only contain lettters"

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address format"

        return errors

    def validate_password(self, postData):
        errors = {}

        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"

        if postData['password'] != postData['pw_confirm']:
            errors['password'] = "Password does not match confirmation"

        return errors



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.BinaryField(max_length=255)
    user_level = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<User object: {} {} {}".format(self.first_name, self.last_name, self.email)

    objects = UserManager()

class Message(models.Model):
    message = models.TextField()
    recipient = models.ForeignKey(User, related_name='messages_recieved', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='messages_sent', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
