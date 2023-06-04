import os
from dotenv import load_dotenv, dotenv_values
from FlightRadar24.api import FlightRadar24API
from FlightRadar24.flight import Flight
from pprint import pprint

load_dotenv()
print("Hello, Python FR24 test")
fr_api = FlightRadar24API()

def get_flight_details(flight_id):
    details = fr_api.get_flight_details(flight_id)
    return details

def write_FlightsList(file_path, FlightsList, thisBound, bounds, airline):
    with open(file_path, 'w') as file:
        file.write("Arreglo de objetos tipo Flight de elementos voladores\n\n")
        file.write("Parámetros petición:\n")
        file.write(f'\tLat Lon Bounds:\n\t\t{bounds} :: aprox {thisBound}\n')
        file.write(f'\tAerolinea:\n\t\t{airline}\n\n')
        file.write(f'- - - - -\n\n')
        file.write(f'Respuesta:\n\n')
        file.write(f'Tamaño:\t{len(FlightsList)}\n\n')
        pprint(FlightsList, stream=file)

def write_flight(file_path, flight):
    with open(file_path, 'w') as file:
        file.write("Un objeto tipo Flight de la lista\n\n")
        file.write(f'Atributos contenidos:\n\t{dir(flight)}\n\n')
        pprint(vars(flight), stream=file)

def write_flight_details(file_path, flightDetails):
    with open(file_path, 'w') as file:
        file.write("JSON de detalles de un vuelo por ID\n\n")
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

def write_fligths_with_destiny(fligthsList, airportIata):
    flightsToDestinyList = [flight for flight in fligthsList if flight.destination_airport_iata == airportIata]
    destiny_file = "Detalles_Vuelos_A_Destino.txt"
    with open(destiny_file,'w') as file:
        file.write("Arreglo detallado de Flight que van al aeropuerto\n\n")
        file.write(f'Aeropuerto:\n\t\t{airportIata}\n\n')
        file.write(f'- - - - -\n\n')
        file.write(f'Respuesta:\n\n')
        file.write(f'Tamaño:\t{len(fligthsList)}\n\n')
        flightsToDestinyDetailsList = [
            {
                'callsign': fl.callsign,
                'registration': fl.registration,
                'aircraft_code': fl.aircraft_code,
                'airline_icao': fl.airline_icao,
                'origin_airport_iata': fl.origin_airport_iata,
                'destination_airport_iata': fl.destination_airport_iata,
                'latitude': fl.latitude,
                'longitude': fl.longitude,
                'time': fl.time,
                # 'airline_iata': 'AV',
                # 'altitude': 0,
                # 'ground_speed': 0,
                # 'heading': 67,
                # 'icao_24bit': 'AD4EBC',
                # 'id': '3094788f',
                # 'number': 'AV8563',
                # 'on_ground': 1,
                # 'squawk': 'N/A',
                # 'vertical_speed': 0
            }
            for fl in flightsToDestinyList
        ]
        pprint(flightsToDestinyDetailsList, stream=file)


def main():
    boundsDict = {
        'colombia' :"18.314,-8.494,-85.97,-58.988",
        'newYork' : "44.719,39.693,-75.268,-68.117",
        'laNada' : "23.817,-2.624,-42.155,-13.548",
        'eldorado' : "4.73,4.676,-74.18,-74.113",
        'america': "55.378,-38.551,-115.187,-17.629",
        'world': "81.906,-64.644,-155.071,171.882"
    }
    thisBound = 'world'
    airline = 'AVA'
    FlightsList = fr_api.get_flights(bounds=boundsDict[thisBound], airline=airline)
    flight = FlightsList[-1]
    flightDetails = fr_api.get_flight_details(flight.id)

    write_FlightsList("Arreglo-de-vuelos-totales.txt", FlightsList, thisBound, boundsDict[thisBound], airline)
    write_flight("Attributos-de-un-vuelo.txt", flight)
    write_flight_details("JSON-detallado-de-un-vuelo.txt", flightDetails)

    write_fligths_with_destiny(FlightsList,'BOG')

    # getZones()

# Executing the main function
if __name__ == "__main__":
    main()




# code to clear terminal screen . código borrar terminal consola
# >>> import os
# >>> clear = lambda: os.system('clear')
# >>> clear()