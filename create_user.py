import boto3
from botocore.exceptions import ClientError
from termcolor import colored
client = boto3.client('iam')
def create_user():
    """
    Create a user "username" with an appropriate permissions (S3VideoReader you've just created)
    """
    while True:
        username = input("Insert username: ")
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
            print("successfully Created User {}".format(username))
            break

        except ClientError as e:
            if e.response['Error']['Code'] == 'EntityAlreadyExists':
                print(colored('User already exists', 'red'))
                print("Please Enter A Different User Name")
            else:
                print("Unexpected error: %s" % e)



if __name__ == '__main__':
    create_user("test1")