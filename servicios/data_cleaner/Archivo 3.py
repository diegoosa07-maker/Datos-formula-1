import os
import csv
import json

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
                    "Escudería": guardar.get("team_name"), #I: Nombre archivo | D: Nombre en URL
                    "Puntos": guardar.get("points_current")
                }
                out.append(fila)

    # comprobar si existe el output directory
    os.makedirs("data/clean", exist_ok=True)
    
  
    fieldnames = ["Escudería", "Puntos"] # Aquí pones el nombre que quieres que tenga el encabezado en el archivo.
    
    with open("data/clean/team_info.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(out)
# Cambiar drivers_list por team_data.csv, tanto arriba como abajo

json_to_csv("data/raw/team_info.json")