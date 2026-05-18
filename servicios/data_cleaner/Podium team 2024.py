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
                    "team_name": guardar.get("team_name"),
                    "position_current": guardar.get("position_current"),
                    "points_current": guardar.get("points_current")
                }
                out.append(fila)
                
    os.makedirs("data/raw", exist_ok=True)
    with open("data/raw/teamspodium2024.json", "w", encoding="utf-8") as f:
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
                    "Escudería": guardar.get("team_name"),
                    "Puntos": guardar.get("points_current")
                }
                out.append(fila)

    os.makedirs("data/clean", exist_ok=True)
    fieldnames = ["Escudería", "Puntos"]
    with open("data/clean/teamspodium2024.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(out)


json_to_json("data/raw/teamspoints2024_data.json")
json_to_csv("data/raw/teamspodium2024.json")