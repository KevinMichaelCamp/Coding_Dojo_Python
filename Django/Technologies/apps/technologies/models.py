from django.db import models

# Create your models here.


class TechnologyManager(models.Manager):
    def validate(self, postData):
        errors = {}

        if len(postData['name']) < 1:
            errors['name'] = "Name cannot be blank"
        if len(postData['tech_type']) < 2:
            errors['tech_type'] = "Technology type must be at least 2 characters"
        if len(postData['purpose']) < 2:
            errors['purpose'] = "Purpose must be at least 2 characters"
        if len(postData['release_date']) < 4:
            errors['release_date'] = "Release date cannot be blank"
        if len(postData['imgurl']) < 1:
            errors['imgurl'] = "Image URL cannot be blank"

        return errors


class Technology(models.Model):
    name = models.CharField(max_length=255)
    tech_type = models.CharField(max_length=255)
    purpose = models.TextField(null=False, blank=False)
    release_date = models.IntegerField()
    imgurl = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Tech object: {} {} {}".format(self.name, self.tech_type, self.release_date)

    objects = TechnologyManager()
