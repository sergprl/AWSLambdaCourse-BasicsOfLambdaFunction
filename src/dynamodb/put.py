import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    response = client.put_item(
        TableName='RetailSales',
        Item={
            'CostumerID': {
                'S': '001',
            },
            'Product': {
                'S': 'Mangos',
            },
            'CustomerID': {
                'N': '100',
            },
            'Address': {
                'S': '161 Loco Road',
            }
        },
    )

    print(response)


