import json
import boto3
client=boto3.client('s3')

def lambda_handler(event, context):
    list_s3=client.list_buckets()

    print(list_s3['Buckets'])
