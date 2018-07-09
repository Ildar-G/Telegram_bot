import requests
import misc
import json


weather_key = misc.weather_key


def get_weather_updates(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=' + weather_key
    r = requests.get(url)
    return r.json()

def weather_save(city):
    data = get_weather_updates(city)
    with open('weather_update.json', 'w') as file:
        json.dump(data, file, indent=2)


def extract_weather(city):
    data = get_weather_updates(city)

    temp = float(data['main']['temp'] - 273.15)
    humidity = data['main']['humidity']
    city_name = data['name']
    city_country = data['sys']['country']
    weather = [city_name, city_country, round(temp, 2), humidity]
    return weather

weather_save('London')
