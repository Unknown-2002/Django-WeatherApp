import datetime
import requests

from django.shortcuts import render


# # Create your views here.
# def index(request):
#     # API_KEY = open("C:\\Users\\lmleo\\Documents\\Django-WeatherApp\\weather_project\\weather_app\\API_KEY", "r").read()
#     API_KEY = 'ac0752f440a23c56c6dd548b02d6bc7e'
#     current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
#     #forecast_url = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}'
#     # current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
#     # forecast_url = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}'

#     if request.method == "POST":
#         city1 = request.POST['city1']
#         city2 = request.POST.get('city2', None)

#         weather_data1, daily_forecast1 = fetch_weather_and_forecast(city1, API_KEY, current_weather_url, forecast_url)

#         if city2:
#             weather_data2, daily_forecast2 = fetch_weather_and_forecast(city2, API_KEY, current_weather_url, forecast_url)
#         else:
#            weather_data2, daily_forecast2 = None

#         context = {
#             "weather_data1": weather_data1,
#             "daily_forecast1": daily_forecast1,
#             "weather_data2": weather_data2,
#             "daily_forecast2": daily_forecast2
#         }
#         return render(request, "weather_app/index.html")

#     else:
#         return render(request, "weather_app/index.html")

# Below functions used to get information in the index.html(endpoint): when have the post request(fetch info)

# def fetch_weather_and_forecast(city, API_KEY, current_weather_url, forecast_url):
#     response = requests.get(current_weather_url.format(city, API_KEY)).json() #send the request to the url and get the json form object (#format of the response)
#     lat, lon = response['coord']['lat'], response['coord']['lon'] #latitube and longtitube
#     forecast_response = requests.get(forecast_url.format(lat, lon, API_KEY)).json()

#     # weather_data = {
#     #     "city": city,
#     #     "temperature": round(response['main']['temp'] - 273.15, 2), #to get celcius and do in 2 decimal place
#     #     "description": response['weather'][0]['description'],
#     #     "icon": response['weather'][0]['icon']
#     # }

#     weather_data = {
#         'city': city,
#         'temperature': round(response['main']['temp'] - 273.15, 2),
#         'description': response['weather'][0]['description'],
#         'icon': response['weather'][0]['icon'],
#     }

#     daily_forecast = []
#     for daily_data in forecast_response['daily'][:5]: #from the response get the json object(key value "dt")
#         daily_forecast.append({ #doing disctionary to append into list
#             "day": datetime.datetime.fromtimestamp(daily_data['dt']).string("%A"), #dt which has the info of timestamp
#             "min_temp":round(daily_data['temp']['min' - 273.15, 2]), 
#             "max_temp":round(daily_data['temp']['max' - 273.15, 2]),
#             "description": daily_data['weather'][0]['decription'],
#             "icon": daily_data['weather'][0]['icon']
#         })

#     return weather_data, daily_forecast

def fetch_weather(city, API_KEY, current_weather_url):
    # Fetch current weather data
    response = requests.get(current_weather_url.format(city, API_KEY)).json()
    weather_data = {
        'city': city,
        'temperature': round(response['main']['temp'] - 273.15, 2),
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
    }
    return weather_data

def index(request):
    API_KEY = 'ac0752f440a23c56c6dd548b02d6bc7e'
    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

    if request.method == "POST":
        city1 = request.POST['city1']
        city2 = request.POST.get('city2', None)

        weather_data1 = fetch_weather(city1, API_KEY, current_weather_url)
        weather_data2 = fetch_weather(city2, API_KEY, current_weather_url) if city2 else None

        context = {
            "weather_data1": weather_data1,
            "weather_data2": weather_data2,
        }
        return render(request, "weather_app/index.html", context)
    else:
        return render(request, "weather_app/index.html")
    


