FROM python:3.8-slim-buster

WORKDIR /flask_app

COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements/requirements.txt



CMD [ "python3", "-m" , "flask", "run"]