from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from current_conditions.forms import LocationForm

def index(request):
    current_temp = '70F'
    wunderground_url_base = 'http://api.wunderground.com/api/3bb1446cf63dc3d0/conditions/q/'
    # default zip code
    zip_code = 20009

    if request.method == 'POST':
        zip_form = LocationForm(request.POST)
        if zip_form.is_valid():
            zip_code = zip_form.cleaned_data['zip_code']
        
    else:
        zip_form = LocationForm()


    request_url = wunderground_url_base + str(zip_code) + '.json'

    r = requests.get(request_url)
    r = r.json()

    conditions = {'Temperature' : r['current_observation']['temperature_string'],
                    'Feels Like' : r['current_observation']['feelslike_string'],
    }
    location = r['current_observation']['observation_location']['full']
    
    ## !!! This part here will fail if the request doesn't go right, so you should figure out a way to handle that! :-)
    return render(request, 'current_conditions/index.html', {'location' : location, 
                                                            'conditions' : conditions,
                                                            'zip_form' : zip_form,
                                                            })