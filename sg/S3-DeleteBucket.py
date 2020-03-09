import boto3
import boto3.session
session = boto3.session.Session(profile_name='webscale')
endpoint = 'http://172.16.0.167:8084'
s3 = session.resource(service_name='s3', endpoint_url=endpoint)
client = s3.meta.client

# Create a Bucket as test
s3.Bucket('test').create()

# List all buckets
for bucket in s3.buckets.all():
    print(bucket.name)


# Delete a Bucket
s3.Bucket('test').delete()

for bucket in s3.buckets.all():
    print(bucket.name)
