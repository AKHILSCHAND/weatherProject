from django.shortcuts import render
import urllib.request
import json

# Create your views here.
def home(request):
    if request.method == 'POST':
        city = request.POST.get('city').strip()  # Remove leading/trailing spaces
        if city !="":
            api_url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + urllib.parse.quote(city) + '&units=metric&appid=987e31fd75f978dd2df3cdf8da52234e').read()
            api_url_dict = json.loads(api_url)

            data = {
                "country": city,
                "weather_description": api_url_dict['weather'][0]['description'],
                "weather_temperature": api_url_dict['main']['temp'],
                "weather_pressure": api_url_dict['main']['pressure'],
                "weather_humidity": api_url_dict['main']['humidity'],
                "weather_icon": api_url_dict['weather'][0]['icon'],
            }
            context = {
                "city": city,
                "data": data,
                
            }
        else:
            return render(request, 'home.html')
    else:
        city = None
        data = {}

    return render(request, 'home.html', context)