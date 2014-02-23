from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):
    current_temp = '70F'
    wunderground_url_base = 'http://api.wunderground.com/api/3bb1446cf63dc3d0/conditions/q/'
    city = 'Seoul'
    country = 'Korea'
    location = city + ', ' + country

    request_url = wunderground_url_base + country + '/' + city + '.json'
    r = requests.get(request_url)
    r = r.json()

    current_temp = r['current_observation']['temperature_string']
    return HttpResponse("Current temperature in %s is %s." % (location, current_temp))
