import json
import boto3
client=boto3.client('ec2')

def lambda_handler(event, context):
    response = client.start_instances(
        InstanceIds=[
            'i-0848e489a43f31db6',
        ],
    )

    print(response['StartingInstances'][0]['InstanceId'])