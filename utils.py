import json

import boto3

bucket_name = 'nimble-flask-test-bucket'


def create_client(profile_name):
    session = boto3.Session(profile_name=profile_name)
    s3_client = session.client('s3')

    return s3_client


def get_data_from_s3(key):
    s3 = create_client('Pashok')
    data_object = s3.get_object(Bucket=bucket_name, Key='data.json')
    data_in_bytes: bytes = data_object['Body'].read()
    data: dict = json.loads(data_in_bytes)
    if data.get(key):
        return str(data[key])
    else:
        return 'Нет такого ключа!'


def get_all_data_from_s3():
    s3 = create_client('Pashok')
    data_object = s3.get_object(Bucket=bucket_name, Key='data.json')
    data_in_bytes: bytes = data_object['Body'].read()
    return json.loads(data_in_bytes)


def save_to_s3(file_name):
    s3 = create_client('Pashok')
    s3.upload_file(Filename=file_name, Bucket=bucket_name, Key=file_name)
