import boto3
from botocore.exceptions import ClientError
client = boto3.client('iam')
def create_user():
    """
    Create a user "username" with an appropriate permissions (S3VideoReader you've just created)
    """
    while True:
        username=input("insert username: ")
        try:
            response = client.create_user(
                UserName= username,
                PermissionsBoundary='arn:aws:iam::955114013936:policy/S3VideoReader',
                Tags=[
                    {
                        'Key': 'YoutubeAppSub',
                        'Value': '1'
                    },
                ]
            )
            print("Created user: {}".format(username))
        except ClientError as e:
            if e.response['Error']['Code'] == 'EntityAlreadyExists':
                print("User already exists")
                print("Please Enter a Different username!")
            else:
                print("Unexpected error: %s" % e)



if __name__ == '__main__':
    create_user("test1")