import boto3
import boto3.session

session = boto3.session.Session(aws_access_key_id="CILQ8MI0OVQHT8NA1164",
                                aws_secret_access_key="YgsmU2c612zCknfjGTjvgrBqYQPwd2GUCzJ62K6m")
endpoint = 'http://172.16.0.164:8084'
s3 = session.resource(service_name='s3', endpoint_url=endpoint)
client = s3.meta.client

# update a new object to a bucket
# obj = s3.Object('3-3','vm.tar.gz')
# obj.upload_file('/root/vm.tar.gz')

# MyBucket = s3.Bucket('3-2')
# for myBucketObject in MyBucket.objects.all():
#    print(myBucketObject.key)

for MyBucket in s3.buckets.all():

    print('Bucket Name is: ', MyBucket.name)

    for myBucketObject in MyBucket.objects.all():
        print(myBucketObject.key)
