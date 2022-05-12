## Cronos
### Prueba


Crear un mini portal web de fondos de pantalla Desktop que pueda adaptarse a responsive.
Cada fondo tendrá:
_ Un título
_ Una descripción corta
_ Un precio
_ Una imagen descargable en 1366x768 (carpeta "/imgs/download")
_ Una imagen miniatura en 136x76 (carpeta "/imgs/preview")
_ Una flag que indica si está activa o no.

Criterios:
1. Las imágenes deben ser procesadas para guardar 2 versiones en los tamaños definidos
2. Cada versión de imagen en una carpeta diferente.
3. El original puede mantenerse o descartarse a elección del desarrollador.
4. La vista pública será una grilla de miniaturas con título y precio de las imágenes activas.
5. Al dar click a la miniatura, se pasa a una vista ampliada del fondo con todos sus datos y un link de descarga directa.
6. Las imágenes se cargan a través de un formulario del admin de Django.
7. Se debe usar motor de BD Postgresql para almacenamiento del modelo.
8. El proyecto debe correr sobre Docker, ya sea todo autocontenido en un solo contenedor o con docker-compose.
9. Entregar en un repo el código con su Dockerfile/compose para ser descargado y levantado con Docker.
10. Webserver preferentemente Nginx.
11. Inicializar el repo público al iniciar el desarrollo para llevar tracking de tiempo de finalización.


## El formato en el cual guardar las imágenes resultantes debe ser ".webp"



### Comandos utilizados:


python3 manage.py makemigrations

python3 manage.py sqlmigrate fondo 0001

python3 manage.py migrate



************************************

CREATE DATABASE fondospantalla


Borrar base de datos

	select application_name,client_hostname,pid,usename from pg_stat_activity where datname='fondospantalla';


	select pg_terminate_backend(pid) from pg_stat_activity where pid='';


Docker

	sudo docker-compose up --build

	sudo systemctl stop docker

	sudo systemctl stop docker.socket


Migrate

    sudo docker-compose up --build
    
    sudo docker-compose run django_app python FondosPantalla/manage.py makemigrations
    
    sudo docker-compose run django_app python FondosPantalla/manage.py migrate
    
    sudo docker-compose run django_app python FondosPantalla/manage.py collectstatic