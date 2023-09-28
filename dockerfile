# Usa una imagen base de Python
FROM python:3.8

# Copia los archivos del proyecto al contenedor
COPY . /app

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Especifica el comando para ejecutar tu aplicación
CMD ["python", "run.py"]
