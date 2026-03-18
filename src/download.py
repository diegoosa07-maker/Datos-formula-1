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


# drivers
drivers_url = "https://api.openf1.org/v1/drivers?session_key=9693"
drivers_data = api_request(drivers_url)
drivers_file_path = "data/raw/drivers_data.json"
data_writing(drivers_file_path, drivers_data)

# Teams 2025: Tomo los datos obtenidos tras la finalización de la carrera final de 2025 para así quedarme únicamente con los puntos finales de cada escudería.
team_url = "https://api.openf1.org/v1/championship_teams?session_key=9839"
team_data = api_request(team_url)
team_file_path = "data/raw/team_info.json"
data_writing(team_file_path, team_data)

# Sessions 2025
sessions_2025_url = "https://api.openf1.org/v1/sessions?year=2025&session_type=Race"
sessions_2025_data = api_request(sessions_2025_url)
data_writing("data/raw/sessions_2025.json", sessions_2025_data, "w")

# drivers (2024): Para obtener los datos finales de cada piloto del año 2024 debo extraer los datos de la carrera final (session_key=9662)
drivers_2024_url = "https://api.openf1.org/v1/championship_drivers?session_key=9662" 
drivers_2024_data = api_request(drivers_2024_url)
drivers_2024_file_path = "data/raw/drivers_2024_data.json"
data_writing(drivers_2024_file_path, drivers_2024_data)

# Pilotos-Escuderías:
equipos_url = "https://api.jolpi.ca/ergast/f1/current/driverStandings.json"
equipos_data = api_request(equipos_url)
equipos_file_path = "data/raw/equipos_data.json"
data_writing(equipos_file_path, equipos_data)