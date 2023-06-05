import os
from dotenv import load_dotenv, dotenv_values
from FlightRadar24.api import FlightRadar24API
from FlightRadar24.flight import Flight
import requests
import time
from pprint import pprint

load_dotenv()
traccarID = 666

# manual data
def manualDataInput():
    lat = 11.017700;
    lon = -74.795400;
    return lat,lon

def getFlightAttributesFromArray(bounds, airline, flightNumber):
    # constants
    BOUNDS_DICT = {
        'colombia' :"18.314,-8.494,-85.97,-58.988",
        'newYork' : "44.719,39.693,-75.268,-68.117",
        'laNada' : "23.817,-2.624,-42.155,-13.548",
        'eldorado' : "4.73,4.676,-74.18,-74.113",
        'america': "55.378,-38.551,-115.187,-17.629",
        'world': "81.906,-64.644,-155.071,171.882"
    }
    # get all flights of given 'airline' inside 'bounds'
    flightsList = FlightRadar24API().get_flights(bounds=BOUNDS_DICT[bounds], airline=airline)
    # take the flights to 'destiny'
    # flightsToDestinyList = [flight for flight in flightsList if flight.destination_airport_iata == destiny]
    # take the flight element in the array with callsign = flightNumber
    fl = [fl for fl in flightsList if fl.callsign == flightNumber][0]
    if (fl):
        return {
                'id': fl.id,
                'callsign': fl.callsign,
                'registration': fl.registration,
                'aircraft_code': fl.aircraft_code,
                'airline_icao': fl.airline_icao,
                'origin_airport_iata': fl.origin_airport_iata,
                'destination_airport_iata': fl.destination_airport_iata,
                'latitude': fl.latitude,
                'longitude': fl.longitude,
                'time': fl.time
        }
    else:
        return 'no hay una verga'

def urlBuilding(traccarID, dataDict):
    # build an url of the form: f'http://gps.sighums.com:5055/?id={traccarID}&{param1}={value1}&{param2}={value2}&{paramX}={valueX}
    url = f''
    return url

# data send
def sendToTraccar(url):
    requests.get(url)

def main():
    # action loop
    idx = 0
    while True:
        # variables load
        # # from manualDataInput
        
        # # from getFlightDetailsWithID

        # # from getFlightAttributesFromArray
        dataDict = getFlightAttributesFromArray()

        # # URL bulding
        url = urlBuilding(traccarID, dataDict)
        sendToTraccar(url)

        pprint(f'idx:{idx}, pos:{lat,lon}')
        # loop end
        time.sleep(3)
        idx = idx + 1


dataDict = getFlightAttributesFromArray('world','AVA','AVA019')
pprint(dataDict)

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