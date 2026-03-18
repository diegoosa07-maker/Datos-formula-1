import os
import json

def json_to_json(file_path):
    out = []
    diccionario = crear_diccionario_drivers('data/raw/drivers2023_data.json')
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() and ( line.strip() == "[" or line.strip() == "]" or line.strip() == ""):
                continue
            else :
                guardar = json.loads(line.strip())
                driver_number = guardar.get("driver_number")
                fila = {
                    "driver_number": driver_number,
                    "broadcast_name": diccionario.get(driver_number, "Unknown"),
                    "position_current": guardar.get("position_current"),
                    "points_current": guardar.get("points_current"),
                }
                out.append(fila)
    os.makedirs("data/raw", exist_ok=True)
    with open("data/raw/driverspoints2023.json", "w", encoding="utf-8") as f:
        for fila in out:
            f.write(json.dumps(fila) + "\n")

def crear_diccionario_drivers(file_path):
    diccionario = {}
    with open(file_path, "r") as fIn:
        for line in fIn:
            line = json.loads(line)
            diccionario[line['driver_number']] = line['broadcast_name']
    return diccionario

json_to_json("data/raw/driverspoints2023_data.json")