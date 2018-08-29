from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from register.models import User


# Create your views here.
def index(request):
    user = User(userID='1',email='JacobTamUs@gmail.com',password='tam',date_joined=datetime.now())
    user.save()
    return HttpResponse("SUCCESS")