FROM python:3.10-slim

WORKDIR /app

# Copia e instala solo las librerías del descargador
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el script download.py a la imagen
COPY . .

# Comando por defecto: ejecuta la descarga directamente
CMD ["python", "download.py"]