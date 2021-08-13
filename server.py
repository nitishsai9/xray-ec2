import boto3
from aws_xray_sdk.core import xray_recorder, patch_all
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

from flask import Flask

app = Flask(__name__)
xray_recorder.configure(service='Flask_ec2')

XRayMiddleware(app, xray_recorder)
patch_all()

@app.route('/s3buckets')
def callAWSSDK():
    client = boto3.client('s3')
    client.list_buckets()

    return 's3bucketcall working fine'

@app.route('/')
def checker():
  return 'healthcheck!'
if __name__ == '__main__':
  app.run(host="127.0.0.1",port='80',debug=True)
