from django.db import models

class Blob(models.Model):
    name = models.CharField(max_length=45)
    team = models.CharField(max_length=45)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
