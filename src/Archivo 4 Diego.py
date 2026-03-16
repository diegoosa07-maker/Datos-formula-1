import os
import json
import requests

def api_request(url):
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

def data_writing(file_path, data, mode="w"):
    os.makedirs("data/raw", exist_ok=True)
    
    with open(file_path, mode, encoding="utf-8") as f:
        for element in data:
            f.write(json.dumps(element) + "\n")
            
    print(f"Se guardaron {len(data)} elementos en {file_path}")

f1_url = "https://api.openf1.org/v1/sessions?year=2025&session_type=Race"
f1_data = api_request(f1_url)
data_writing("data/raw/sessions_2026.json", f1_data, "w")