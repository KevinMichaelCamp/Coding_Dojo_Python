from __future__ import unicode_literals
from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = "Course name must be at least 5 characters long"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Course object: {}".format(self.name)

    objects = CourseManager()

class DescriptionManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['desc']) < 10:
            errors['desc'] = "Description must be at least 10 characters long"
        return errors

class Description(models.Model):
    desc = models.TextField()
    course = models.OneToOneField(Course, related_name='description', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Description object: {} {}".format(self.desc, self.course)

    objects = DescriptionManager()

class Comment(models.Model):
    comment = models.TextField()
    course = models.ForeignKey(Course, related_name='comments', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Comment object: {} {}".format(self.coment, self.course)
