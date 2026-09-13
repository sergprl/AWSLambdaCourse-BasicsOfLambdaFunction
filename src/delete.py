import json
import boto3
client=boto3.client('s3')

def lambda_handler(event, context):
    delete_bucket = client.delete_bucket(
        Bucket='udemydemo12345'
    )

    print(delete_bucket)
    print("deleted bucket udemydemo12345")