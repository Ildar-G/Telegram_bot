import requests
import misc
import json

weather_token = misc.weather_token


city = ''
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=' + weather_token


def get_weather_updates(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=' + weather_token
    r = requests.get(url)
    print(url)
    return r.json()

def weather_save(city):
    data = get_weather_updates(city)

    with open('weather_update.json', 'w') as file:
        json.dump(data, file, indent=2)

def extract_weather(city):
    data = get_weather_updates(city)
    weather = {data['main']['temp'], data['sys']['country']}
    return weather


get_weather_updates('London')
weather_save('London')
#e = extract_weather('London')

#print (e)
#print (type(e))
