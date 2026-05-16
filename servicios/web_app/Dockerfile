FROM python:3.10-slim

WORKDIR /app

# Copia e instala las librerías de la interfaz web (ej: streamlit)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el script interface.py
COPY . .

# Comando por defecto: arranca tu aplicación web
CMD ["python", "interface.py"]