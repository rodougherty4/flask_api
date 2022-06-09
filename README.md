# Device reading API

Instructions on how to start up your application 
requirements :
1. Docker installed
2. python installed
3. git installed

run the following in terminal:

***

git clone https://github.com/rodougherty4/flask_api.git

cd flask_api

docker build -t reading_api:latest .

docker run -d -p 1234:1234 reading_api:latest

python flask/test_reading_api/test_reading_api.py

***

List the HTTP endpoints exposed by your application and any required parameters
* HTTP endpoint = "http://127.0.0.1:1234/reading"

Any notes on design decisions 
* chose flask, but may consider fastapi
* may not be optimal persistance layer
* decided to persist all valid api calls (duplicate included). This may help with analytics and troubleshooting.

Anything you would have included given more time

* create pytest unit tests
* structure code better
* deploy docker image registry and share built image