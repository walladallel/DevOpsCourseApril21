import boto3
import botocore

# My username to be created
UNA="noamst1"

#Create_user function
def create_user():
    iam = boto3.client("iam")
    response = iam.list_users()
    print(response)




create_user()
