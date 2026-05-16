FROM python:3.10-slim

WORKDIR /app

# Copia e instala las librerías necesarias para limpiar (ej: pandas)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos tus archivos de limpieza y el orquestador run_pipeline.py
COPY . .

# Comando por defecto: arranca el orquestador que correrá los 7 scripts en orden
CMD ["python", "run_pipeline.py"]