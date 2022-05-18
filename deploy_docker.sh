#bin\bash

docker build --tag flask-docker-app:v1.0 flask_app

docker run -p 5000:5000 flask-docker-app:v1.0
