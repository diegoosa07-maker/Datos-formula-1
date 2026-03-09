import os 
import json
import requests

def api_requests(url):
    response = requests.get(url)
    return response.json()

def data_writing(file_path, data, mode="w"):
    os.makedirs("data/raw", exist_ok=True)

    with open(file_path, mode, encoding="utf-8") as f:
        f.write(json.dumps(element) + "\n")

# equipos
equipos_url = "https://api.jolpi.ca/ergast/f1/current/driverStandings.json"
equipos_data = api_requests(equipos_url)
equipos_file_patch = "data/raw/equipos_data.json"


data_writing(equipos_file_path, equipos_data)





