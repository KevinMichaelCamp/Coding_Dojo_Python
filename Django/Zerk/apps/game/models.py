from django.db import models

import bcrypt
import re

EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'[a-zA-Z\s]+$')

class UserManager(models.Manager):
    def validate_login(self, postData):
        errors = {}

        if len(User.objects.get(email=postData['email'])):
            user = User.objects.get(email=postData['email'])
            if bcrypt.checkpw(postData['password'].encode(), user.password):
                return errors
            else:
                errors['password'] = "Password incorrect"
                return errors
        else:
            errors['email'] = "Email not found in database"

    def validate_reg(self, postData):
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
            errors['email'] = "Email already exists in database"

        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        elif postData['password'] != postData['pw_confirm']:
            errors['password'] = "Password does not match confirmation"

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

class Race(models.Model):
    race = models.CharField(max_length=255)
    max_health = models.SmallIntegerField()
    max_strength = models.SmallIntegerField()
    max_magic = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Race object: {} {} {}".format(self.race, self.max_health, self.max_strength)

class Character(models.Model):
    user = models.ForeignKey(User, related_name='characters', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    race = models.ForeignKey(Race, related_name='characters', on_delete=models.CASCADE)
    money = models.SmallIntegerField(default=0)
    health = models.SmallIntegerField()
    strength = models.SmallIntegerField()
    magic = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Character object: {} {} {} {} {} {} {} {}".format(self.user, self.name, self.sex, self.race, self.money, self.health, self.strength, self.magic)
