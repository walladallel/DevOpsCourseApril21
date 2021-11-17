import boto3
from datetime import datetime, timezone

string = "test"

def get_user_age_seconds(user_create_date):

    client = boto3.client('iam')

    response = client.get_user(
        UserName= string
    )

    print(response)
    return (datetime.now(timezone.utc) - user_create_date).total_seconds()
get_user_age_seconds(string)

