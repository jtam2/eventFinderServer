from django.conf.urls import url
from events.views import careerlaunch_scrap

urlpatterns = [
        url(r'^careerlaunch$', careerlaunch_scrap.careerLaunch, name='careerLaunch')
    ]
