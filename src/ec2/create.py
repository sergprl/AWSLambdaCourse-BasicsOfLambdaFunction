import json
import boto3
client=boto3.client('ec2')

def lambda_handler(event, context):
    response = client.run_instances(
        ImageId='ami-0354c98ae10b02961',
        InstanceType='t3.micro',
        MaxCount=1,
        MinCount=1,
    )

    print(response['Instances'][0]['InstanceId'])
    