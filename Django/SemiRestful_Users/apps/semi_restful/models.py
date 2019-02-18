from __future__ import unicode_literals
from django.db import models

# Create your models here.

class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors['first_name'] = "First name may not be blank"
        if len(postData['last_name']) < 1:
            errors['last_name'] = "Last name may not be blank"
        if len(postData['email']) < 1:
            errors['email'] = "Email name may not be blank"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    
    def __repr__(self):
        return "<User object: {} {} {}".format(self.first_name, self.last_name, self.email)
