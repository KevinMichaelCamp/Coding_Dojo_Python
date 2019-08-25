from django.db import models
import bcrypt
import re

NAME_REGEX = re.compile(r'[a-zA-Z\s]+$')
EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA_Z0-9._-]+\.[a-zA-z]+$')


class UserManager(models.Manager):
    def validate_register(self, postData):
        errors = {}

        if len(postData['first_name']) <  2:
            errors['first_name'] = "First name must be at least 2 characters"
        elif not NAME_REGEX.match(postData['first_name']):
            errors['first_name'] = "First name can only contain letters"

        if len(postData['last_name']) <  2:
            errors['last_name'] = "Last name must be at least 2 characters"
        elif not NAME_REGEX.match(postData['last_name']):
            errors['last_name'] = "Last name can only contain letters"

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email format"
        elif len(User.objects.filter(email=postData['email'])):
            errors['email'] = "Email already in use"

        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"

        if postData['password'] != postData['pw_confirm']:
            errors['pw_confirm'] = "Password does not match confirmation"

        return errors


    def validate_login(self, postData):
        errors = {}

        if len(User.objects.filter(email=postData['email'])):
            user = User.objects.get(email=postData['email'])
            if bcrypt.checkpw(postData['password'].encode(), user.password):
                return errors
            else:
                errors['login'] = "Invalid Email/Password"
                return errors
        else:
            errors['login'] = "Invalid Email/Password"
            return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.BinaryField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<User object: {} {} {}".format(self.first_name, self.last_name, self.email)

    objects = UserManager()


class Friendship(models.Model):
    friend = models.ForeignKey(User, related_name='friends', on_delete=models.CASCADE)
    friended_by = models.ForeignKey(User, related_name='friended_bys', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Friend object: {} {}".format(self.friend, self.friended_by)
