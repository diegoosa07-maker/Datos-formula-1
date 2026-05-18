import subprocess
import sys

def ejecutar_script(script_path):
    print(f" Ejecutando: {script_path}")
    # Ejecuta el script y espera a que termine
    resultado = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
    
    if resultado.returncode == 0:
        print(f" {script_path} finalizado con éxito.")
        print(resultado.stdout)
    else:
        print(f" Error en {script_path}:")
        print(resultado.stderr)
        sys.exit(1) # Detiene todo el contenedor si un script falla

if __name__ == "__main__":
    print("INICIANDO PIPELINE DE LIMPIEZA")
    
    # Lista ordenada de tus scripts de limpieza
    pipeline = [
        "Archivo 1.py",
        "archivo 2.py",
        "Archivo 3.py",
        "Archivo 4.py",
        "Podium 2023.py",
        "Archivo 6.py",
        "Podium 2024.py",
        "Podium 2025.py",
        "Podium team 2023.py",
        "Podium team 2024.py",
        "Podium team 2025.py",
        "Calendario 2023.py",
        "Calendario 2024.py",
        "Calendario 2025.py",
        "Calendario 2026.py"
        ]
    for script in pipeline:
        ejecutar_script(script)
        
    print("PIPELINE FINALIZADO CON ÉXITO")