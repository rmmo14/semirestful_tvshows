from django.db import models
from datetime import datetime

# Create your models here.
class myManager(models.Manager):
    def my_validator(self, postData):
        errors = {}
        errors['required'] = ""
        if len(postData['title']) < 2:
            errors['title'] = "The title should be at least 2 characters"
            errors['required'] = "All fields required"
        if len(postData['network']) < 3:
            errors['network'] = "The network should be at least 3 characters"
            errors['required'] = "All fields required"
        if len(postData['description']) < 10:
            errors['description'] = "The description should be at least 10 characters"
            errors['required'] = "All fields required"
        if datetime.strptime(postData['release_date'], '%Y-%m-%d') > datetime.now():
            errors['release_date'] = 'Release Date should be in the past'
        return errors

class tvShow(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = myManager()