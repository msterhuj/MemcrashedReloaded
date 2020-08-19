import flask
import iptools


app = flask.Flask(__name__)
iter = iptools.IpRangeList('192.93.0.0/16').__iter__()


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
