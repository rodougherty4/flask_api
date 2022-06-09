FROM python:3.8.13

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .


ENTRYPOINT [ "python" ]
CMD [ "/python-docker/flask/reading_api.py" ]
