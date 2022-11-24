from django.db import models
from django.utils import timezone

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=225)

class Post(models.Model):
    subject = models.CharField(max_length=225)
    content = models.CharField(max_length=225)
    author = models.CharField(max_length=20)
    create_date = models.DateField(default=timezone.now)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)