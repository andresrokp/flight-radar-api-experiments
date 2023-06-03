import os
from dotenv import load_dotenv, dotenv_values
from FlightRadar24.api import FlightRadar24API
from FlightRadar24.flight import Flight
from pprint import pprint

load_dotenv()
print("hello python fr24 test")
fr_api = FlightRadar24API()

def holaMundo():
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


def writeInFiles():
    flightsssPure = fr_api.get_flights()
    flight = flightsssPure[-1]
    flightDetails = fr_api.get_flight_details(flight.id)

    flightsssPure_file = "Arreglo-de-vuelos-totales.txt"
    flight_file = "Attributos-de-un-vuelo.txt"
    flight_details_file = "JSON-detallado-de-un-vuelo.txt"

    with open(flightsssPure_file,'w') as file:
        file.write("Arreglo de objetos tipo Flight de elementos voladores\n")
        file.write(f'Tamaño:\n\t{len(flightsssPure)}\n\n')
        pprint(flightsssPure, stream=file)

    with open(flight_file,'w') as file:
        file.write("Un objeto tipo Fligth de la lista\n")
        file.write(f'Atributos contenidos:\n\t{dir(flight)}\n\n')
        pprint(vars(flight), stream=file)

    with open(flight_details_file,'w') as file:
        file.write("JSON de detalles de un vuelo por ID\n")
        file.write(f'Tamaño:\n\t{len(flightDetails)}\n')
        file.write(f'Propiedades contenidas:\n\t{flightDetails.keys()}\n\n')
        pprint(flightDetails, stream=file)

def getZones():
    zones_list = fr_api.get_zones()    
    zones_file = "Lista-zonas-de-vuelo.txt"

    with open(zones_file,'w') as file:
        file.write("Dict de zonas\n")
        file.write(f'Tamaño:\n\t{len(zones_list)}\n')
        file.write(f'Propiedades contenidas:\n\t{zones_list.keys()}\n\n')
        pprint(zones_list, stream=file)

def main():
    # writeInFiles()
    getZones()

# exec
main()



# code to clear terminal screen . código borrar terminal consola
# >>> import os
# >>> clear = lambda: os.system('clear')
# >>> clear()