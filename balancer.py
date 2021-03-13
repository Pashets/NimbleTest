import random
from flask import redirect, Flask, request
import requests

app = Flask(__name__)

ips = [
    '127.0.0.1:5000',
    '127.0.0.1:5001'
]


@app.route('/items/<string:key>', methods=['GET'])
def get_data(key: str):
    return redirect('http://' + random.choice(ips) + f'/items/{key}')


@app.route('/items/<string:key>', methods=['PUT'])
def put_data(key):
    data = request.json
    response = requests.put('http://' + random.choice(ips) + f'/items/{key}', json=data)
    return response.text


if __name__ == '__main__':
    app.run()
