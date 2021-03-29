#utiliza la version 3.10 de python
FROM python:3.10.0a6-slim-buster

#establece el 'working directory'
WORKDIR /app

#copia todos los archivos necesarios para la app
#todo lo local ('.') a /app ('.')
COPY . .

#instala los requerimientos necesarios
RUN pip3 install -r requirements.txt

#etiqueta para mostrar el puerto en el que se sirve el contenedor
EXPOSE 5000

#ejecuta la aplicacion
CMD ["python3", "redis-app.py"]
