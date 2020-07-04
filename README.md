# Python Serverless Template

## Requirements
- docker is installed
- pipenv is installed
- npm is installed
- AWS user with efficent roles to manage lambdas, RDS

## Run locally
- initialize virtual env ```pipenv shell```
- install dependencies ```pipenv install```
- copy .env.sample to .env and fill in all variables
- start local database ```docker-compose up -d database```
- migrate local database ```python manage.py db upgrade```
- run flask app ```flask run```

## Add git hooks
To prevent formatting conflicts I would strongly suggest to use "black" via git hooks
- setup git hooks via ```python -m python_githooks```

## Deploy to AWS
- install serverless packages ```npm install```
- ensure that the AWS variables are set correctly in .env and run ```source .env```
- deploy by running ```sls deploy```

## Change data model
- adjust the model in models.py
- create new migration ```python manage.py db migrate```
- edit new migration if needed

## Migrate remote database
- go to AWS => Lambda => Environment variables => use the database host and port ini your .env file
- source your .env file ```source .env```
- migrate database ```python manage.py db upgrade```

## Run serverless locally
- the following command will emulate a local lambda environment ```sls offline```