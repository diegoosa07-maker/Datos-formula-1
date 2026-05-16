import os
import csv
import json
# Voy a quedarme con la información de circuito_short_name, country_name, location, date_start y date_end, así como session_type y session_name
def json_to_csv(file_path):
    out = []
    
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            # limpiar lineas
            if line.strip() and (line.strip() == "[" or line.strip() == "]" or line.strip() == ""):
                continue
            else:
                guardar = json.loads(line.strip())
                
               # nombre del conductor y su equipo
                fila = {
                    "Tipo de Carrera": guardar.get("session_name"), #I: Nombre archivo | D: Nombre en URL
                    "Comienzo": guardar.get("date_start"),
                    "Fin": guardar.get("date_end"),
                    "Nombre del Circuito": guardar.get("circuit_short_name"),
                    "País": guardar.get("country_name"),
                    "Ubicación": guardar.get("location")
                }
                out.append(fila)

    # comprobar si existe el output directory
    os.makedirs("data/clean", exist_ok=True)
    
  
    fieldnames = ["Tipo de Carrera", "Comienzo", "Fin", "Nombre del Circuito", "País", "Ubicación"] # Aquí pones el nombre que quieres que tenga el encabezado en el archivo.
    
    with open("data/clean/sessions_2025.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(out)
# Cambiar drivers_list por team_data.csv, tanto arriba como abajo

json_to_csv("data/raw/sessions_2025.json")