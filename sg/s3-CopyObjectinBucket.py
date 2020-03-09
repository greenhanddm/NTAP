import boto3
import boto3.session

session = boto3.session.Session(profile_name='webscale')
endpoint = 'http://172.16.0.167:8084'
s3 = session.resource(service_name='s3', endpoint_url=endpoint)
client = s3.meta.client

for MyBucket in s3.buckets.all():

    if MyBucket.name is not 3 - 4:

        print('Bucket Name is: ', MyBucket.name)

        for myBucketObject in MyBucket.objects.all():
            objname = str(myBucketObject.key)
            print(objname)
            tarobjname = '{}'.format(objname[:-4])
            tarobjexname = '{}'.format(objname[-4:])
            copied_obj = s3.Object(MyBucket.name, tarobjname + 'new' + tarobjexname)
            copied_obj.copy_from(CopySource='/' + MyBucket.name + '/' + myBucketObject.key)
