import boto3
iam_client = boto3.client('iam')
try:
    un = "noamsyt"
    iam_client.create_user(iam_client)
        UserName="un",
    except ClientError as error:
        print("Unexpected error ")
    return 'User could not be created’,error



def create_user(username):
        iam = boto3.client("iam")
        response = iam.create_user(UserName=username)
        print(response)