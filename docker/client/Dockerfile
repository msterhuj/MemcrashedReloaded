FROM python:3.8.5-buster

ENV MONGO_URL="mongodb://mongo:27017/"
ENV MONGO_DB_NAME="ipisinthisdb"

WORKDIR /app

COPY . /app

RUN pip3 install requests ntplib iptools pymongo

CMD [ "python3", "client.py" ]