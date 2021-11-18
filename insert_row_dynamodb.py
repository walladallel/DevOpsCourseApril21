import boto3

client = boto3.client('dynamodb')

client.put_item(
    TableName='',
    Item={}
)
