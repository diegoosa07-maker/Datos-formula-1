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
<<<<<<< Updated upstream
            f.write(json.dumps(element) + "\n")
=======
          f.write(json.dumps(element) + "\n")


# equipos 2025
equipos_url = "https://api.jolpi.ca/ergast/f1/2025/driverStandings.json"
equipos_data = api_request(equipos_url)
equipos_file_path = "data/raw/equipos_data.json"



data_writing(equipos_file_path, equipos_data)
    
>>>>>>> Stashed changes

# drivers 2025
drivers_url = "https://api.openf1.org/v1/drivers?year=2025"
drivers_data = api_request(drivers_url)
drivers_file_path = "data/raw/drivers_data.json"

data_writing(drivers_file_path, drivers_data)

# resultados de carreras 2025
sessions_url = "https://api.openf1.org/v1/sessions?year=2025&session_type=Race"
sessions_data = api_request(sessions_url)

for session in sessions_data:
    session_key = session.get("session_key")
    
    # posiciones (session_key no funciona)
    positions_url = f"https://api.openf1.org/v1/position?session_key={session_key}"
    positions_data = api_request(positions_url)
    data_writing(f"data/raw/positions_{session_key}.json", positions_data)
    
    # drivers por sesion
    drivers_url = f"https://api.openf1.org/v1/drivers?session_key={session_key}"
    drivers_session_data = api_request(drivers_url)
    data_writing(f"data/raw/drivers_{session_key}.json", drivers_session_data)