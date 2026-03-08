import os 
import json 
import requests

# Primeramente y como hicimos en el proyecto anterior, pedimos la url.
# Esta función es casi idéntica a la de clase, excepto que no requerimos un ACCESS TOKEN porque esta es pública.
def api_request(url):
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

# Una vez más, reutilizo el código hecho en clase, las notas asociadas estan en el otro archivo.    
def data_writing(file_path, data,mode="w"):
    
    os.makedirs("data/raw", exist_ok=True)

    with open(file_path, mode,  encoding="utf-8") as f:
        for element in data:
            f.write(json.dumps(element) + "\n")

        # La principal diferencia entre este código y el de clase, aparte de las url, es que no uso otro archivo registro POR AHORA.
        print(f"Se guardaron {len(data)} elementos en {file_path}")

# Las URL para que funcionen el programa:
f1_url = "http://api.jolpi.ca/ergast/f1/current/constructorStandings.json"
f1_data = api_request(f1_url)


# Parte IA: Por algún motivo, mi programa parecía no ser capaz de crear el archivo, así que solicité la ayuda de la IA para esta parte.
if f1_data:
    # Navegamos por el JSON para llegar a la lista de puntos
    # La ruta es: MRData -> StandingsTable -> StandingsLists[primer elemento] -> ConstructorStandings
    standings_list = f1_data["MRData"]["StandingsTable"]["StandingsLists"][0]["ConstructorStandings"]
    
    f1_file_path = "data/raw/team_info.json"
    
    # Guardamos los datos
    data_writing(f1_file_path, standings_list)