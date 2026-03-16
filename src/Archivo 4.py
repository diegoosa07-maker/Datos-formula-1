import os
import csv
import json

def json_to_csv(positions_file, drivers_file, output_file):
    drivers_map = {}
    with open(drivers_file, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip() or line.strip() in ("[", "]"):
                continue
            d = json.loads(line.strip())
            if isinstance(d, dict):
                drivers_map[d.get("driver_number")] = d

    # obtener ultima posicion de cada piloto
    final_positions = {}
    with open(positions_file, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip() or line.strip() in ("[", "]"):
                continue
            p = json.loads(line.strip())
            if isinstance(p, dict):
                final_positions[p.get("driver_number")] = p.get("position")

    out = []
    for driver_number, position in final_positions.items():
        guardar = drivers_map.get(driver_number, {})

        fila = {
            "Posicion": position,
            "Piloto": guardar.get("broadcast_name"),
            "Dorsal": driver_number,
            "Scuderia": guardar.get("team_name"),
            "Session_Key": guardar.get("session_key")
        }
        out.append(fila)

    # ordenar por posicion
    out.sort(key=lambda x: x["Posicion"] if x["Posicion"] else 99)

    os.makedirs("data/clean", exist_ok=True)

    fieldnames = ["Posicion", "Piloto", "Dorsal", "Scuderia", "Session_Key"]

    with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(out)


# procesar todos los archivos de posiciones
for file in os.listdir("data/raw"):
    if file.startswith("positions_"):
        session_key = file.replace("positions_", "").replace(".json", "")
        drivers_file = f"data/raw/drivers_{session_key}.json"
        if os.path.exists(drivers_file):
            json_to_csv(
                f"data/raw/{file}",
                drivers_file,
                f"data/clean/race_results_{session_key}.csv"
            )
