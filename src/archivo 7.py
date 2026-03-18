import os
import csv
import json
import requests

if not os.path.exists("data/clean"):
    os.makedirs("data/clean")

url = "https://api.jolpi.ca/ergast/f1/2025/driverStandings.json"

respuesta = requests.get(url)
datos_json = respuesta.json()

lista_pilotos = datos_json["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]

f = open("data/clean/archivo_7.csv", "w", encoding="utf-8", newline="")
writer = csv.writer(f)
writer.writerow(["posicion", "puntos", "piloto"])

for p in lista_pilotos:
    nombre = p["Driver"]["givenName"] + " " + p["Driver"]["familyName"]
    puntos = p["points"]
    pos = p["position"]
    
    writer.writerow([pos, puntos, nombre])

f.close()