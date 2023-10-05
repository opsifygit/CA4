# Connecting to the docker container

Connect to the docker image on PORT 27017

## Building the Image

docker build -t db:latest .

## Running the Image

docker run -p 27017:27017 db

## String for connection

mongodb://localhost:27017/
