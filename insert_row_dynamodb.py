import boto3

client = boto3.client('dynamodb', region_name='us-east-1')

client.put_item(
    TableName='students',
    Item={
        'username': {
            'S': 'yoramB'
        },
        'age': {
            'N': '34'
        },
        "status": {
            'S': "married"
        }
    }
)
