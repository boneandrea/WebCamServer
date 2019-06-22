import boto3
import sys
import os
from dotenv import load_dotenv


def init_s3():
    load_dotenv()
    return boto3.client('s3',
                        region_name='ap-northeast-1'
                        )


if __name__ == '__main__':
    s3 = init_s3()

    s3.list_buckets()
    obj = s3.get_object(Bucket='knuckle-images', Key='abc.txt')
#bucket = s3.Bucket('knuckle-images')
#obj = bucket.Object('abc.txt').get()

    print(obj['Body'].read().decode("utf-8"))
