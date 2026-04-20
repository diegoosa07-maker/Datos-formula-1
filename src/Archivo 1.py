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
                    "Piloto": guardar.get("broadcast_name"),
                    "Escuderia": guardar.get("team_name")
                }
                out.append(fila)

    # comprobar si existe el output directory
    os.makedirs("data/clean", exist_ok=True)
    
  
    fieldnames = ["Piloto", "Scuderia"]
    
    with open("data/clean/drivers_list.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(out)


json_to_csv("data/raw/drivers_data.json")