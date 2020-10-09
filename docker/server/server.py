import iptools
import os
from flask import Flask, request


app = Flask(__name__)
iter = iptools.IpRangeList(os.getenv("IP_RANGE_LIST")).__iter__()


@app.route('/next', methods=['GET'])
def next_ip_pool():
    try:
        global iter
        ip = iptools.next(iter)
        return str(ip)
    except StopIteration:
        return "end"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
