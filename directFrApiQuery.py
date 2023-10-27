import requests

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
        print(data)
    else:
        print("BAD")
except requests.exceptions.RequestException as e:
    print('VERY BAD\n',e)