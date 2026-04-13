import os
import json
import requests

def api_request(url):
    response = requests.get(url)
    return response.json()

def data_writing(file_path, data_to_save):
    os.makedirs("data/raw", exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        # Aquí estaba el error: usamos data_to_save que es lo que recibe la función
        f.write(json.dumps(data_to_save) + "\n")

# --- EQUIPOS ---
equipos_url = "https://api.jolpi.ca/ergast/f1/current/driverStandings.json"
equipos_data = api_request(equipos_url) # Corregido: api_request en singular
equipos_file_path = "data/raw/equipos_data.json"
data_writing(equipos_file_path, equipos_data)

# --- DRIVERS (PILOTOS) ---
drivers_url = "https://api.openf1.org/v1/drivers?session_key=latest"
drivers_data = api_request(drivers_url)
drivers_file_path = "data/raw/drivers_data.json"
data_writing(drivers_file_path, drivers_data)

print(" Datos descargados correctamente")