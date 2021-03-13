import json

from flask import Flask, request

from utils import get_data_from_s3, get_all_data_from_s3, save_to_s3

app = Flask(__name__)


@app.route('/items/<string:key>', methods=['GET'])
def get_data(key: str):
    return get_data_from_s3(key)


@app.route('/items/<string:key>', methods=['PUT'])
def put_data(key):
    old_data = get_all_data_from_s3()
    data = request.json
    old_data[key] = data['value']
    with open('data.json', 'w') as f:
        json.dump(old_data, f)
    save_to_s3('data.json')
    return '200'


if __name__ == '__main__':
    app.run()
