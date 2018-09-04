from django.shortcuts import render
from django.http import HttpResponse
from django.db import IntegrityError

from events.models import Events, EventTypes

import mechanicalsoup
import string
import datetime
from time import strptime
# Create your views here.
POSSIBLE_TYPES = ['accounting', 'marketing']

def index(request):
    return HttpResponse('HELLO FROM EVENT')

def careerLaunch(request):
    browser = careerLaunchLogin()
    browser.follow_link("events")
    #scrapping
    containers = browser.get_current_page().find_all("li", {"class": "event_item"})
    table = str.maketrans(dict.fromkeys(string.punctuation))

    for container in containers:
        #grab the date of event
        date_container = container.p.find_all('span',{'class':'event-date'})
        unclean_date = date_container[0].text
        date_array = unclean_date.split()
        month_name = date_array[1].translate(table)
        month_num = strptime(month_name, '%B').tm_mon
        day = date_array[2].translate(table)
        year = date_array[3].translate(table)

        date = datetime.datetime(int(year), int(day), month_num)

        #grab the time
        time_container = container.p.find_all('span',{'class':'event-time'})
        time = time_container[0].text
        #grab the event title
        event_title_container = container.find_all('div',{'class':'title'})
        event_title = event_title_container[0].text
        #grab event types
        event_type = []
        for word_unclean in event_title.split():
            word = word_unclean.translate(table)
            if word in POSSIBLE_TYPES:
                event_type.append(word)
        #grab the location of event
        location_container = container.p.find_all('span',{'class':'location'})
        location = location_container[0].text
    
        #add Event to Database:
        try:
            event = Events.objects.create(school='byu', address=location, date=date, time=time, title=event_title)

            #add event type into Database
            for different_type in event_type:
                EventTypes.objects.create(eventType=different_type, event=event)

        except IntegrityError as e:
            print("ERROR (careerLaunch Scraping):")
            print(e.__cause__)


def careerLaunchLogin():
    browser = mechanicalsoup.StatefulBrowser()
    browser.open('https://careerlaunch.byu.edu/account/login/')
    browser.select_form('form[action="https://careerlaunch.byu.edu/account/login/authenticate/"]')
    browser["user_login"] = 'jacobtamus@hotmail.com'
    browser.submit_selected()

    browser.select_form('form[method="POST"]')
    browser["user_password"] = "tam967596"
    browser.submit_selected()

    return browser
