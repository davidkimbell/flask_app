# Forecastio library
import forecastio
from geopy.geocoders import Nominatim

# OS library
import os

# Python dotenv
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_weather(address):
    api_key = os.environ['FORECASTIO_API_KEY']
    # api_key = '45cb745df4eb44129be9a5a22d8f0733'
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude
    forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
    summary = forecast.summary
    temperature = forecast.temperature
    return "{} and {}° at {}".format(summary, temperature, address)