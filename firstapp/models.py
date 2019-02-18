from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    image = models.ImageField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
