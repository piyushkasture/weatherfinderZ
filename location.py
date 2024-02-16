import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('API_KEY')

@dataclass
class weatherData:
    city: str
    country: str
    main: str
    description: str
    icon: str
    temperature: int
    minimum_temperature: int
    maximum_temperature: int
    humidity: int
    speed: float

def get_location(city_name, state_code, country_code, api_key):
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={api_key}').json()

    data = resp[0]
    lat = data.get('lat')
    lon = data.get('lon')

    return lat, lon

def get_current_weather(lat, lon, api_key):

    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric').json()

    data = weatherData(
        city=resp.get('name'),
        country = resp.get('sys').get('country'),
        main = resp.get('weather')[0].get('main'),
        description = resp.get('weather')[0].get('description'),
        icon = resp.get('weather')[0].get('icon'),
        temperature = resp.get('main').get('temp'),
        minimum_temperature = resp.get('main').get('temp_min'),
        maximum_temperature = resp.get('main').get('temp_max'),
        humidity = resp.get('main').get('humidity'),
        speed = resp.get('wind').get('speed')
    )
    return data

def main(city_name, state_code, country_code):
    lat, lon = get_location(city_name, state_code, country_code, api_key)
    weather_data = get_current_weather(lat, lon, api_key)
    return weather_data


if __name__=='__main__':
    lat, lon = get_location('Pune', 'MH', 'INDIA', api_key) # (40.7128, -74.006)
    print(get_current_weather(lat, lon, api_key))


# print(get_location('New York', 'NY', 'US', api_key)) # <Response [401]>
