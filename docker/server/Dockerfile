FROM python:3.8.5-buster

ENV IP_RANGE_LIST="192.168.0.0/24"

WORKDIR /app

COPY . /app

RUN pip3 install iptools flask

CMD [ "python3", "server.py" ]