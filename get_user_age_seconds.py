import boto3
from datetime import datetime, timezone

usern = input("Please Enter a user name: ")


def get_user_age_seconds(user_create_date):

    client = boto3.client('iam')

    response = {}
    response = client.get_user(
        UserName= usern,
    )


    print(response)



#    user_create_date = User["CreateDate"]
    user_create_date = response['User']['CreateDate']
    print(user_create_date)

   # return (datetime.now(timezone.utc) - user_create_date).total_seconds()

get_user_age_seconds(usern)
