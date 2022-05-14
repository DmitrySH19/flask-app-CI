#bin\bash

docker build --tag flask-docker-app:v1.0 flask_app

docker run flask-docker-app:v1.0
