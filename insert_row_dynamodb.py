import boto3

client = boto3.client('dynamodb')

client.put_item(
    TableName='students',
    Item={
        'studentId': {
            'S': '123'
        },
        'name': {
            'S': 'alon'
        },
        'lastname': {
            'S': 'itach'
        }
    }
)
