import boto3
import boto3.session

session = boto3.session.Session(aws_access_key_id="CILQ8MI0OVQHT8NA1164",
                                aws_secret_access_key="YgsmU2c612zCknfjGTjvgrBqYQPwd2GUCzJ62K6m")
endpoint = 'http://172.16.0.164:8084'
s3 = session.resource(service_name='s3', endpoint_url=endpoint)
client = s3.meta.client
