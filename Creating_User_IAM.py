import boto3
import botocore

# My username to be created
UNA="noamst1"

#Create_user function
def create_user():
    try:
        iam = boto3.client("iam")
        response = iam.create_user(UserName=UNA)
        print(response)
    except:
        print("Error")




create_user()
