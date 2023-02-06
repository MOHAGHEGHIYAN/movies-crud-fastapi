# movies-crud-fastapi

A simple CRUD movie app powered by FastAPI

## run

At first, install decencies with following commands

`pip install -r requirements.txt`

Then redirect to root directory (that includes main.py), create `.env` file with following settings:

- MYSQL_DB_HOST
- MYSQL_DB_PORT
- MYSQL_DB_USER
- MYSQL_DB_PASS
- MYSQL_DB_NAME

 and execute following command:

`uvicorn main:app --env-file .env`

## initialize database

to initialize the database redirect run following command in root directory:

python -m db_initializer
