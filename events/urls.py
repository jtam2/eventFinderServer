from django.conf.urls import url
from events import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^careerlaunch$', views.careerLaunch, name='careerLaunch')
    ]
