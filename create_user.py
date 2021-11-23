import boto3
from botocore.exceptions import ClientError
from termcolor import colored
client = boto3.client('iam')
def create_user(username):
    """
    Create a user "username" with an appropriate permissions (S3VideoReader you've just created)
    """

    while True:

        try:
            response = client.create_user(
                UserName=username,
                PermissionsBoundary='arn:aws:iam::955114013936:policy/S3VideoReader',
                Tags=[
                    {
                        'Key': 'YoutubeAppSub',
                        'Value': '1'
                    },
                ]
            )
            print("--------------------------------------------")
            print((colored("Successfully Created User {}".format(username), 'green')))
            print("--------------------------------------------")

            break

        except ClientError as e:
            if e.response['Error']['Code'] == 'EntityAlreadyExists':
                print(colored('User already exists', 'red'))
                print("Please Enter A Different User Name")
                username = input("Enter Username: ")
                continue
            else:
                print("Unexpected error: %s" % e)
                continue




if __name__ == '__main__':
    create_user("test1")