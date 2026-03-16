import os
import json
import requests

def api_request(url):
    response = requests.get(url)
    return response.json()

def data_writing(file_path, data, mode="w"):
    os.makedirs("data/raw", exist_ok=True)

    with open(file_path, mode, encoding="utf-8") as f:
        for element in data:
          f.write(json.dumps(element) + "\n")


# drivers
drivers_url = "https://api.openf1.org/v1/drivers?session_key=9693"
drivers_data = api_request(drivers_url)
drivers_file_path = "data/raw/drivers_data.json"

data_writing(drivers_file_path, drivers_data)