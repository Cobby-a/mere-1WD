from django.db import models

# Create your models here.

class features(models.Model):
    author = models.CharField(max_length=100)
    about = models.CharField(max_length=500)
    pages = models.IntegerField(max_length=400)