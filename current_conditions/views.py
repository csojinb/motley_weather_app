from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from current_conditions.forms import LocationForm

def index(request):
    current_temp = '70F'
    wunderground_url_base = 'http://api.wunderground.com/api/3bb1446cf63dc3d0/conditions/q/'

    if request.method == 'POST':
        zip_form = LocationForm(request.POST)
        if zip_form.is_valid():
            zip_code = zip_form.cleaned_data['zip_code']
      
            request_url = wunderground_url_base + str(zip_code) + '.json'

            r = requests.get(request_url)
            r = r.json()

            try:
                weather_description = r['current_observation']['weather']
                weather_description_icon_url = r['current_observation']['icon_url']

                conditions = {'Temperature' : r['current_observation']['temperature_string'],
                                'Feels Like' : r['current_observation']['feelslike_string'],
                                'Dew Point' : r['current_observation']['dewpoint_string'],
                                'Relative Humidity' : r['current_observation']['relative_humidity'],
                                'Wind' : r['current_observation']['wind_string'],
                }
                location = r['current_observation']['observation_location']['full']

                return render(request, 'current_conditions/index.html', {'location' : location, 
                                                                    'conditions' : conditions,
                                                                    'zip_form' : zip_form,
                                                                    'weather_description' : weather_description,
                                                                    'weather_description_icon_url' : weather_description_icon_url
                                                                    })
            except:
                error_msg = r['response']['error']['description']

                return render(request, 'current_conditions/index.html', {'zip_form': zip_form,
                                                                        'error_msg' : error_msg,
                                                                        })

    else:
        zip_form = LocationForm()

    return render(request, 'current_conditions/index.html', {'zip_form': zip_form,
                                                                    })

    