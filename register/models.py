from django.db import models
from events.models import Events
from datetime import datetime
# Create your models here.
class User(models.Model):
    email = models.CharField(unique=True, primary_key=True, max_length=200)
    userID = models.ForeignKey(Events, on_delete=models.CASCADE, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    password = models.CharField(null=True, unique=True, max_length=200)
