from django.shortcuts import render
from django.http import HttpResponse

import mechanicalsoup
import string
# Create your views here.
POSSIBLE_TYPES = ['accounting', 'marketing']

def index(request):
    return HttpResponse('HELLO FROM EVENT')

def careerLaunch(request):
    browser = careerLaunchLogin()
    browser.follow_link("events")
    #scrapping
    containers = browser.get_current_page().find_all("li", {"class": "event_item"})
    for container in containers:
        #grab the date of event
        date_container = container.p.find_all('span',{'class':'event-date'})
        date = date_container[0].text
        #grab the time
        time_container = container.p.find_all('span',{'class':'event-time'})
        time = time_container[0].text
        #grab the event title
        event_title_container = container.find_all('div',{'class':'title'})
        event_title = event_title_container[0].text
        #grab event types
        event_type = []
        table = str.maketrans(dict.fromkeys(string.punctuation))
        for word_unclean in event_title.split():
            word = word_unclean.translate(table)
            if word in POSSIBLE_TYPES:
                event_type.append(word)
        #grab the location of event
        location_container = container.p.find_all('span',{'class':'location'})
        location = location_container[0].text

        #TODO: put all these things into an obj or put it into database probably both.
            #will need to think about how we an event can have multiple types
            

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
