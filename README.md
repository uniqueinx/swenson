# Starting server
## docker-compose
```sh
docker-compose up --build
```
This docker uses the official build for fastapi and preconfigured for production performance

## local
```sh
pip install -r local_requirments
uvicorn main:app
```

# Testing
## pytest
```sh
pytest
```
## curl
```sh
./tests.sh 8080
```
as 8000 is the port server is running on.

#
