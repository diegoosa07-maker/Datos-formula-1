import os
import csv
import json 
import requests 

def json_to_csv(url, output_path):
    # 1. Obtener los datos de la URL
    response = requests.get(url)
    data = response.json()
    
    # 2. Navegar por el JSON hasta la lista de pilotos
    # La ruta es: MRData -> StandingsTable -> StandingsLists[0] -> DriverStandings
    try:
        standings = data ["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]
    except (KeyError, IndexError):
        print("Error: No se pudo encontrar la estructura de datos en el JSON.")
        return

    # 3. Preparar la carpeta de salida (como en tu foto)
    os.makedirs("data/clean", exist_ok=True)
    
    # 4. Definir las columnas que queremos en el CSV
    fieldnames = ["posicion", "puntos", "nombre", "apellido", "constructor"]
    
    # 5. Escribir el archivo (usando la ruta de tu captura)
    with open(output_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for entry in standings:
            # Extraemos la info basada en el JSON que pegaste
            fila = {
                "posicion": entry.get("position", "N/A"),
                "puntos": entry.get("points", "0"),
                "nombre": entry["Driver"].get("givenName"),
                "apellido": entry["Driver"].get("familyName"),
                "constructor": entry["Constructors"][0].get("name") if entry["Constructors"] else "N/A"
            }
            writer.writerow(fila)

    print(f"Archivo guardado con éxito en: {output_path}")

# --- Ejecución ---
url_f1 = "https://api.jolpi.ca/ergast/f1/2025/driverStandings.json"
ruta_final = "data/clean/archivo_2.csv"

json_to_csv(url_f1, ruta_final)