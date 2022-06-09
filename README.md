# Device reading API

* url = "http://127.0.0.1:1234/reading"
* parameters = application/json
{ 
 id: (string) The device identifier. This is a uuid.  readings: [ 
 { 
 timestamp: (string) Timestamp for the reading  in [iso 8601 format](https://en.wikipedia.org/wiki/ISO_8601)  count: (integer) 
 } 
 ] 
}


Instructions on how build docker application 

*requirements* :
1. Docker installed
2. python installed
3. git installed

*build docker image 
run the following in terminal:*

***

git clone https://github.com/rodougherty4/flask_api.git

cd flask_api

docker build -t reading_api:latest .

docker run -d -p 1234:1234 reading_api:latest

***

*testing api in python script (json can be modified here flask/test_reading_api/test_reading_api.py):*

python flask/test_reading_api/test_reading_api.py


*design notes:*
* chose flask, but may consider fastapi
* may not be optimal persistance layer
* decided to persist all valid api calls (duplicate included). This may help with analytics and troubleshooting.

*Given more time*

* create pytest unit tests
* structure code better
* deploy docker image registry and share built image