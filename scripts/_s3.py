import os
import traceback
import pprint

import boto3

s3 = boto3.resource('s3')
s3_client = boto3.client('s3')
pp = pprint.PrettyPrinter(indent=3)

def s3_browse():
    """
    Browse s3's buckets
    """
    print('--- s3_browse ---')
    for bucket in s3.buckets.all():
        pp.pprint(bucket)
        for obj in bucket.objects.all():
            pp.pprint(obj)
            #print("Bucket Name: %s - Resource:%s - VersionId:%s " % (bucket.name, obj.key, obj.VersionId))
    print("\n"*2)

def s3_upload(bucket_name, file_name):
    """
    Upload a file to s3 storage
    """
    print('--- s3_upload ---')
    try:
        file_location = os.getcwd() +"\\data\\"+ file_name

        with open(file_location, 'rb') as data:
            s3.Bucket(bucket_name).put_object(Key=file_name, Body=data)
            print("File %s was uploaded!" % file_name)
        print("\n"*2)
    except:
        print(traceback.format_exc())
        print("File upload was failed! Filename:" +file_name)


def s3_download(bucket_name, file_name):
    """
    Download resource from s3
    """
    print('--- s3_download ---')
    saved_file = 'c:\\tmp\\AAA_'+file_name
    s3.Bucket(bucket_name).download_file(file_name, saved_file)

    print("File %s was downloaded!" % saved_file)

def s3_delete_object_via_resource(bucket_name, file_name):
    """
    Delete bucket object via Resources (higher-level) abstraction
    Resources represent an object-oriented interface
    """
    print('--- s3_delete_object_via_resource ---')
    bucket = s3.Bucket(bucket_name)
    response = bucket.delete_objects(
        Delete={
            'Objects': [
                {
                    'Key': file_name,
                },
            ],
        }
    )
    pp.pprint(response)

def s3_delete_object_via_client(bucket_name, file_name):
    """
    Delete bucket object via Clients (low-level) interface
    """
    print('--- s3_delete_object_via_client ---')
    response = s3_client.delete_object(Bucket=bucket_name, Key=file_name)
    pp.pprint(response)

def run():
    test_file = 'hello.txt'
    bucket_name = 'replace_your_bucket_name'

    s3_browse()
    s3_upload(bucket_name, test_file)
    #s3_delete_object_via_resource(bucket_name, test_file)
    #s3_delete_object_via_client(bucket_name, test_file)
    s3_browse()
    #s3_download(bucket_name, test_file)


if __name__ == '__main__':
    run()
