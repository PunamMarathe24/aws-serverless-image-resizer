import boto3
from PIL import Image
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    download_path = '/tmp/' + key
    upload_path = '/tmp/resized-' + key

    s3.download_file(bucket, key, download_path)

    with Image.open(download_path) as image:
        image = image.resize((200, 200))
        image.save(upload_path)

    s3.upload_file(upload_path, bucket, 'resized-' + key)

    return "Image resized successfully"
