# Device reading API

Instructions on how to start up your application 

docker run -d -p 5000:5000 python-docker


List the HTTP endpoints exposed by your application and any required parameters
* HTTP endpoint = "http://127.0.0.1:105/reading"

Any notes on design decisions 
* chose flask, but may consider fastapi
* may not be optimal persistance layer
* decided to persist all valid api calls (duplicate included). This may help with analytics and troubleshooting.


Anything you would have included given more time

* create actual pytest unit tests
* structure code better
* create a docker registry and share built image