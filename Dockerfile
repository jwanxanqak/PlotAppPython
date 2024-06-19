# Usar una imagen base
FROM python:3.11

## Copiar el archivo requirements.txt al directorio de trabajo en el contenedor
COPY ./requirements.txt /requirements.txt

# Copiar el archivo tempYearly.csv al directorio de trabajo en el contenedor
COPY ./tempYearly.csv /tempYearly.csv

# Establecer el directorio de trabajo en el contenedor
WORKDIR /

# Instalar las dependencias
RUN pip3 install -r requirements.txt

# Copiar el resto de los archivos necesarios para la aplicación
COPY . /

#Informa a Docker que el contenedor escuchará en el puerto 15000 en tiempo de ejecución.
EXPOSE 15000

#Configura el contenedor para que se ejecute como una aplicación Python.
ENTRYPOINT ["python3"]

# Comando para ejecutar la aplicación
CMD ["app/app.py"]