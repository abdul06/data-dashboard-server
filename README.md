# Python backend server
<!--- Repo  https://github.com/abdul06/data-dashboard-server -->

## Local Environment Setup:

## Flask

### Marshmellow serialize for rest api

### sqlalchemy for rest api

## packages
    flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy flask-cors psycopg2 requests SQLAlchemy urllib3

## Run docker and setup database 

```javascipt
$ docker-compose up -d // this will setup docker containers and run in background
$ docker ps //make note of database created
$ docker exec -it data-dashboard-server_db_1 bash // the container name you read after running docker ps
$ \l //showes databases;

$ docker exec -it mydb psql -U postgres -d data_dashboard  // Run psql

$ \c database // Use Database postgres

$ \copy [database table] FROM '[path-to-csv-as-string]' DELIMITER ',' CSV HEADER; // command in cli to copy csv to postgres 
$ \copy netflix_titles FROM '/netflix_titles.csv' DELIMITER ',' CSV HEADER;
```
