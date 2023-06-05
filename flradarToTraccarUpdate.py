import os
from dotenv import load_dotenv, dotenv_values
from FlightRadar24.api import FlightRadar24API
from FlightRadar24.flight import Flight
import requests
import time
from pprint import pprint

load_dotenv()
traccarID = 666
lat = 11.017700;
lon = -74.795400;

def sendToTraccar(url):
    requests.get(url)


idx = 0
while True:
    lat = lat + 0.0003
    lon = lon + 0.0003
    url = f'http://gps.sighums.com:5055/?id={traccarID}&lat={lat}&lon={lon}&pruebas=traccar&lugar=barranquilla&idx={idx}'
    pprint(f'idx:{idx}, pos:{lat,lon}')
    sendToTraccar(url)
    time.sleep(3)
    idx = idx + 1




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