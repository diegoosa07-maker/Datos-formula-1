import os
import json
import requests
import time

def api_request(url):
    headers = {"accept": "application/json"}
    # Delay de 2 segundos para evitar la saturación de la API
    time.sleep(2)
    response = requests.get(url, headers=headers)
    return response.json()

def data_writing(file_path, data, mode = 'w'):
    os.makedirs("data/raw", exist_ok=True)
    with open(file_path, mode, encoding="utf-8") as f:
        for element in data:
            f.write(json.dumps(element) + "\n")
            
    print(f"Se guardaron {len(data)} elementos en {file_path}")


# ======================================= INFORMACIÓN ===================================================

# Información de Pilotos 2023 [Escuderías, broadcast_name, driver_number, etc.]:
drivers2023_url = "https://api.openf1.org/v1/drivers?session_key=9197"
drivers2023_data = api_request(drivers2023_url)
drivers2023_filepath = "data/raw/pilotos2023_info.json"
data_writing(drivers2023_filepath, drivers2023_data)

# Información de Pilotos 2024 [Escuderías, broadcast_name, driver_number, etc.]:
drivers2024_url = "https://api.openf1.org/v1/drivers?session_key=9662"
drivers2024_data = api_request(drivers2024_url)
drivers2024_filepath = "data/raw/pilotos2024_info.json" # Antiguo nombre: data/raw/drivernumber_2024.json
data_writing(drivers2024_filepath, drivers2024_data, "w")

# Información de Pilotos 2025 [Escuderías, broadcast_name, driver_number, etc.]:
drivers2025_url = "https://api.openf1.org/v1/drivers?session_key=9693"
drivers2025_data = api_request(drivers2025_url)
drivers2025_filepath = "data/raw/pilotos2025_info.json" # Antiguo nombre: data/raw/drivers_data.json
data_writing(drivers2025_filepath, drivers2025_data)

# Información de Pilotos 2026 [Escuderías, broadcast_name, driver_number, etc.]: 
drivers2026_url = "https://api.openf1.org/v1/drivers?session_key=11436"
drivers2026_data = api_request(drivers2026_url)
drivers2026_filepath = "data/raw/pilotos2026_info.json" # Antiguo nombre: data/raw/drivers2026_info.json
data_writing(drivers2026_filepath, drivers2026_data)

# ======================================================================================================


# ========================================= PUNTOS ======================================================

# Puntos 2023 de pilotos:
driverspoints2023_url = "https://api.openf1.org/v1/championship_drivers?session_key=9197"
driverspoints2023_data = api_request(driverspoints2023_url)
driverspoints2023_filepath = "data/raw/driverspoints2023_data.json" # Antiguo nombre: data/raw/driverspoints2023_data.json
data_writing(driverspoints2023_filepath, driverspoints2023_data)

# Puntos 2024 de pilotos:
driverspoints2024_url = "https://api.openf1.org/v1/championship_drivers?session_key=9662" 
driverspoints2024_data = api_request(driverspoints2024_url)
driverspoints2024_filepath = "data/raw/driverspoints2024_data.json" # Antiguo nombre: data/raw/drivers_2024_data.json
data_writing(driverspoints2024_filepath, driverspoints2024_data)

# Puntos 2025 de pilotos:
driverspoints2025_url = "https://api.openf1.org/v1/championship_drivers?session_key=9839" 
driverspoints2025_data = api_request(driverspoints2025_url)
driverspoints2025_filepath = "data/raw/driverspoints2025_data.json" # Antiguo nombre: data/raw/drivers_2024_data.json
data_writing(driverspoints2025_filepath, driverspoints2025_data)

# Puntos 2023 de Escuderías:
teamspoints2023_url = "https://api.openf1.org/v1/championship_teams?session_key=9197"
teamspoints2023_data = api_request(teamspoints2023_url)
teamspoints2023_filepath = "data/raw/teamspoints2023_data.json" 
data_writing(teamspoints2023_filepath, teamspoints2023_data)

# Puntos 2024 de Escuderías:
teamspoints2024_url = "https://api.openf1.org/v1/championship_teams?session_key=9662"
teamspoints2024_data = api_request(teamspoints2024_url)
teamspoints2024_filepath = "data/raw/teamspoints2024_data.json" 
data_writing(teamspoints2024_filepath, teamspoints2024_data)

# Puntos 2025 de Escuderías:
teamspoints2025_url = "https://api.openf1.org/v1/championship_teams?session_key=9839"
teamspoints2025_data = api_request(teamspoints2025_url)
teamspoints2025_filepath = "data/raw/teamspoints2025_data.json" # Antiguo nombre: data/raw/team_info.json
data_writing(teamspoints2025_filepath, teamspoints2025_data)

# ====================================================================================================

# ======================================= CARRERAS ===================================================

# Carreras 2026: 
sessiones_2026_url = "https://api.openf1.org/v1/sessions?session_name=Race&year=2026"
sessions_2026_data = api_request(sessiones_2026_url)
sessions_2026_filepath = "data/raw/carreras_2026.json"
data_writing(sessions_2026_filepath, sessions_2026_data, "w")

# Carreras 2025:
sessions_2025_url = "https://api.openf1.org/v1/sessions?year=2025&session_type=Race"
sessions_2025_data = api_request(sessions_2025_url)
sessions_2025_filepath = "data/raw/carreras_2025.json"
data_writing(sessions_2025_filepath, sessions_2025_data, "w")

# Carreras 2024: 
sessiones_2024_url = "https://api.openf1.org/v1/sessions?session_name=Race&year=2024"
sessions_2024_data = api_request(sessiones_2024_url)
sessions_2024_filepath = "data/raw/carreras_2024.json"
data_writing(sessions_2024_filepath, sessions_2024_data, "w")

# Carreras 2023: 
sessiones_2023_url = "https://api.openf1.org/v1/sessions?session_name=Race&year=2023"
sessions_2023_data = api_request(sessiones_2023_url)
sessions_2023_filepath = "data/raw/carreras_2023.json"
data_writing(sessions_2023_filepath, sessions_2023_data, "w")

# ======================================================================================================



