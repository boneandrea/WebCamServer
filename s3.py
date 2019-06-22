import boto3
import sys
import os
from dotenv import load_dotenv

load_dotenv()


def init_s3():
    return boto3.client('s3',
                        region_name='ap-northeast-1')


def upload(original_img, bucket, img):
    s3 = boto3.resource('s3',
                        region_name='ap-northeast-1')

    return s3.meta.client.upload_file(original_img, bucket, img)


if __name__ == '__main__':
    s3 = init_s3()

    s3.list_buckets()
    obj = s3.get_object(Bucket='knuckle-images', Key='abc.txt')
    # bucket = s3.Bucket('knuckle-images')
    # obj = bucket.Object('abc.txt').get()

    print(obj['Body'].read().decode("utf-8"))

    upload("hello.txt", 'knuckle-images', 'images/hello5.txt')
