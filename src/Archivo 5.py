import os
import csv
import json

def json_to_csv(file_path):
    out = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() and ( line.strip() == "[" or line.strip() == "]" or line.strip() == ""):
                continue
            else:
                guardar = json.loads(line.strip())
                fila = {
                    "Nombre": guardar.get("broadcast_name"),
                    "Puntos": guardar.get("points_current")
                }
                out.append(fila)

    os.makedirs("data/clean", exist_ok=True)
    fieldnames = ["Nombre", "Puntos"]
    with open("data/clean/driverspoints2023_list.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(out)

json_to_csv("data/raw/driverspoints2023.json")