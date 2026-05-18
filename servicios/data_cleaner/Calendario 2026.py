import os
import json
import csv

def json_to_json(file_path):
    out = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() and (line.strip() == "[" or line.strip() == "]" or line.strip() == ""):
                continue
            else:
                guardar = json.loads(line.strip())
                fila = {
                    "circuit_short_name": guardar.get("circuit_short_name"),
                    "country_name": guardar.get("country_name"),
                    "date_start": guardar.get("date_start"),
                    "year": guardar.get("year"),
                    "is_cancelled": guardar.get("is_cancelled")
                }
                out.append(fila)
                
    os.makedirs("data/raw", exist_ok=True)
    with open("data/raw/calendario2026.json", "w", encoding="utf-8") as f:
        for fila in out:
            f.write(json.dumps(fila) + "\n")

def json_to_csv(file_path):
    out = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() and (line.strip() == "[" or line.strip() == "]" or line.strip() == ""):
                continue
            else:
                guardar = json.loads(line.strip())
                fila = {
                    "Circuito": guardar.get("circuit_short_name"),
                    "País": guardar.get("country_name"),
                    "Fecha Inicio": guardar.get("date_start"),
                    "Año": guardar.get("year"),
                    "Cancelado": guardar.get("is_cancelled")
                }
                out.append(fila)

    fieldnames = ["Circuito", "País", "Fecha Inicio", "Año", "Cancelado"]
    with open("data/clean/calendario2026.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(out)

json_to_json("data/raw/carreras_2026.json")
json_to_csv("data/raw/calendario2026.json")