import boto3
import boto3.session
session = boto3.session.Session(profile_name='webscale')
endpoint = 'http://172.16.0.167:8084'
s3 = session.resource(service_name='s3', endpoint_url=endpoint)
client = s3.meta.client

# update a new object to a bucket
obj = s3.Object('3-3','vm.tar.gz')
obj.upload_file('/root/vm.tar.gz')
