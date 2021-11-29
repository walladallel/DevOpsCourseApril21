import boto3
from botocore.exceptions import ClientError
client = boto3.client('iam')
username=input("Enter UserName:")
response = client.create_user(
    UserName=username,
    PermissionsBoundary='arn:aws:iam::955114013936:policy/S3VideoReader',
    Tags=[
        {
            'Key': 'YoutubeAppSubscriber',
            'Value': username
        },
    ]
)


password=input("Enter Password:")
response1 = client.create_login_profile(
    UserName=username,
    Password=password,
    PasswordResetRequired=False
)

response4 = client.add_user_to_group(
    GroupName='Youtube_Sub_Group',
    UserName=username

)
print(response4)