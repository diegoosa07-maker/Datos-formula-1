# Este código es un versión modificada del archivo clean hecho en clase, los comentarios se encuentran en ese mismo archivo.
# Nota: Recuerda revisar download.
import os
import csv
import json

def crear_diccionario_pilotos(file_path):
    diccionario = {}
    with open(file_path, "r", encoding="utf-8") as fIn:
        for line in fIn:
            line = line.strip()
            
            if line.endswith(","):
                line = line[:-1]
            if line and line not in ["[", "]"]:
                datos = json.loads(line)
                
                diccionario[datos['driver_number']] = datos['broadcast_name']
    return diccionario

def json_to_csv_f1(file_path):
    out = []
    diccionario = crear_diccionario_pilotos('data/raw/drivernumber_2024.json')

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.endswith(","):
                line = line[:-1]
                
            if line and line not in ["[", "]"]:
                guardar = json.loads(line)
                n_identificacion = guardar.get("driver_number")
                nombre_piloto = diccionario.get(n_identificacion, n_identificacion)

                fila = {
                    "Piloto": nombre_piloto,
                    "Calificación Final": guardar.get("position_current"),
                    "Puntos": guardar.get("points_current")
                }
                out.append(fila)
    
    
    fieldnames = ["Piloto", "Calificación Final", "Puntos"]
    with open("data/clean/drivers_data_2024.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(out)


json_to_csv_f1("data/raw/drivers_2024_data.json")