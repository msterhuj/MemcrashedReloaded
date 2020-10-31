FROM python:3.8.5-buster

ENV IP_RANGE_LIST="192.168.0.0/24"
ENV MONGO_URL="mongodb://mongo:27017/"
ENV MONGO_DB_NAME="ipisinthisdb"

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

CMD [ "python3", "TouDoum.py" ]