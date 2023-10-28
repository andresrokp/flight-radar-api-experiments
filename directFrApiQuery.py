import requests
import json
from tabulate import tabulate

headers = {
    "accept-encoding": "gzip, br",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "origin": "https://www.flightradar24.com",
    "referer": "https://www.flightradar24.com/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "accept": "application/json"
}

url = "https://api.flightradar24.com/common/v1/airport.json?code=VER&plugin[]=schedule&plugin-setting[schedule][mode]=arrivals&plugin-setting[schedule][timestamp]=1698425478&limit=100&page=1"

try:
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data,indent=4))
        out_file = 'arrivals.json'
        with open(out_file,'w') as arrivals_file:
            json.dump(data, arrivals_file, indent=4)
        
        # Extract relevant information for arrivals
        arrivals_data = data["result"]["response"]["airport"]["pluginData"]["schedule"]["arrivals"]["data"]
        # Define a bucket list to store data as rows
        table_data = []

        # Iterate through the arrivals and extract relevant information
        for arrival in arrivals_data:

            #get macro properties
            flight = arrival.get("flight", {})
            identification = flight.get("identification", {})
            status = flight.get("status", {})
            aircraft = flight.get("aircraft", {})
            owner = flight.get("owner", {})
            airline = flight.get("airline", {})
            airport = flight.get("airport", {})
            time = flight.get("time", {})

            # Extracting relevant sub properties
            flight_id = identification.get("id", "N/A")
            flight_number = identification.get("number", {}).get("default", "N/A")
            airline_name = airline.get("name", "N/A")
            origin = airport.get("origin", {}).get("name", "N/A")
            destination = airport.get("destination", {}).get("name", "N/A")
            departure_time = time.get("real", {}).get("departure", "N/A")
            arrival_time = time.get("real", {}).get("arrival", "N/A")
            status_text = status.get("text", "N/A")

            # Append the extracted data as a row in the bucket list
            table_data.append([flight_id, flight_number, airline_name, origin, destination, departure_time, arrival_time, status_text])

        # Headers in normal write style
        headers = ["ID", "Flight Number", "Airline", "Origin", "Destination", "Departure Time", "Arrival Time", "Status"]

        # Print the formatted table
        print(tabulate(table_data, headers, tablefmt="fancy_grid"))

    else:
        print("BAD")
except requests.exceptions.RequestException as e:
    print('VERY BAD\n',e)