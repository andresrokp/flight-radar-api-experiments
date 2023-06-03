import os
from dotenv import load_dotenv, dotenv_values
from FlightRadar24.api import FlightRadar24API
from FlightRadar24.flight import Flight
from pprint import pprint

load_dotenv()
print("hello python fr24 test")


fr_api = FlightRadar24API()
flightsssPure = fr_api.get_flights()
flight = flightsssPure[-1]
flightDetails = fr_api.get_flight_details(flight.id)
pprint(flightDetails["identification"])



def test_get_flight_details():
    flight = fr_api.get_flights()[-1]
    details = fr_api.get_flight_details(flight.id)
    return details




print('\n- - - details\n',flightDetails.keys())
# dict_keys(['identification', 'status', 'level', 'promote', 'aircraft', 'airline', 
# 'owner', 'airspace', 'airport', 'flightHistory', 'ems', 'availability', 'time', 
# 'trail', 'firstTimestamp', 's'])

print('\n- - - status\n',flightDetails["status"])
print('\n- - - airport\n')
pprint(flightDetails["airport"])

# code to clear terminal screen . código borrar terminal consola
# >>> import os
# >>> clear = lambda: os.system('clear')
# >>> clear()