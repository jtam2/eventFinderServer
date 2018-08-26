from django.db import models

# Create your models here.
class Events(models.Model):
    city = models.CharField(null=True, max_length=200)
    school = models.CharField(null=True, max_length=50)
    address = models.CharField(null=True, max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    eventType = models.CharField(null=True, max_length=50)