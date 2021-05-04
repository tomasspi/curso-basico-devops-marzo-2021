# Desafio final del curso de DevOps

Para darle un cierre a las clases de Craftech, los invitamos a intentar completar estas pequeñas tareas que resumen lo visto en el curso!

### Resumen

Se cuenta con el diseño de una aplicación para prestamos por internet. El backend fue construido con [Django](https://www.djangoproject.com/) utilizando [Python v3.7](https://www.python.org/), la cual se encuentra [acá](backend/) y el frontend fue construido con [React.js](https://es.reactjs.org/), la cual se encuentra [acá](frontend/).

Se necesita:

1. Armar un diagrama de los componentes que se involucran (Base de datos, deployments, etc) como si estuviera deployado en AWS;

Para despliegue en EKS, se propone la siguiente topología:

<img src="imgs/aws-deploy.png" width="300">

2. Dockerizar las aplicaciones Frontend y Backend;

Se creó un *Dockerfile* para cada componente. Para construir la imagen deseada se deben ingresar los siguientes comandos:

```bash
$ cd <directorio>
$ docker build -t <app-name>:<tag> .
```
donde: `<directorio>` es 'backend' o 'frontend', `<app-name>` es el nombre que se le desee dar a la aplicación y `<tag>` la versión de la misma.

3. Armar un docker-compose que nos permita levantar la aplicación entera y sus dependencias;

<img src="imgs/docker.png" width="300">

En la imagen superior se muestra los servicios creados por *docker compose*:

	- *Backend*;
	- *Base de datos*: [PostgreSQL](https://www.postgresql.org/);
	- *Frontend*.

Para lanzar los servicios se debe ingresar la siguiente linea (en caso de querer re-construir las impagenes utilizar la opción `--build`:

```bash
$ docker-compose up
```

4. Armar los manifiestos de Kubernetes para deployar las aplicaciones y sus dependencias en un cluster (Utilizar minikube como ref);

5. Diseñar un pipeline de CI/CD de la aplicación frontend y backend que nos permita deployar en 2 entornos (dev y prod).
