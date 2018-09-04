from django.db import models

# Create your models here.
class Events(models.Model):
    school = models.CharField(blank=True, null=True, max_length=50)
    address = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True)
    date = models.DateField(null=True)
    time = models.CharField(blank=True, null=True, max_length=100)
    title = models.CharField(max_length=200, null=True, unique=True)

class EventTypes(models.Model):
    eventType = models.CharField(blank=True, null=True, max_length=50)
    event = models.ForeignKey(
        Events, on_delete=models.CASCADE, null=True)
