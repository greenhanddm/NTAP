import boto3
import boto3.session

session = boto3.session.Session(aws_access_key_id="Z0Y6EUUVXS2I4ELME5KR",
                                aws_secret_access_key="BlpFaMQFnk4ym7leMAnqJB5QCELMPGee/CznHNiu")
endpoint = 'http://rtlshsg-gw1.remotelab.com:8084'
s3 = session.resource(service_name='s3', endpoint_url=endpoint)
client = s3.meta.client

# Create new bucket
# s3.Bucket('3-3').create()

# List all buckets
for bucket in s3.buckets.all():
    print(bucket.name)
