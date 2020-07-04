# Python Serverless Template

## Requirements
- docker is installed
- pipenv is installed

## Run locally
- initialize virtual env ```pipenv shell```
- install dependencies ```pipenv install```
- copy .env.sample to .env and fill in all variables
- start local database ```docker-compose up -d database```
- create database "jobs"
- migrate database ```python manage.py db migrate```
- upgrade database ```python manage.py db upgrade```
- run flask app ```python app.py```
