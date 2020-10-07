import iptools
import os
from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
iter = iptools.IpRangeList(os.getenv("IP_RANGE_LIST")).__iter__()

client = MongoClient(os.getenv("MONGO_URL"))
db = client[os.getenv("MONGO_DB_NAME")]

print(os.getenv("MONGO_URL"))


@app.route('/next', methods=['GET'])
def next_ip_pool():
    try:
        global iter
        ip = iptools.next(iter)
        return str(ip)
    except StopIteration:
        return "end"


@app.route('/save', methods=['POST'])
def save():
    if request.is_json:
        data = request.get_json()
        db.reviews.insert_one(data)
        return "Saved on server"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
