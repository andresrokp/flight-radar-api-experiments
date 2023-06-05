import os
from dotenv import load_dotenv, dotenv_values
from FlightRadar24.api import FlightRadar24API
from FlightRadar24.flight import Flight
import requests
import time
from pprint import pprint

load_dotenv()
traccarID = 666
lat = 11.0051;
lon = -74.8080;

def sendRequest(url):
    requests.get(url)


url = f'http://gps.sighums.com:5055/?id={traccarID}&lat={lat}&lon={lon}&pruebas=traccar&lugar=barranquilla'
while True:
    lat = lat + 0.0001
    lon = lon + 0.0001
    pprint({lat,lon})
    sendRequest(url)
    time.sleep(2)




# Vuelo que viene de barcelona
#  {'aircraft_code': 'B788',
#   'airline_icao': 'AVA',
#   'callsign': 'AVA019',
#   'destination_airport_iata': 'BOG',
#   'id': '3094788f',
#   'latitude': 41.29,
#   'longitude': 2.08,
#   'origin_airport_iata': 'BCN',
#   'registration': 'N792AV',
#   'time': 1685967436},