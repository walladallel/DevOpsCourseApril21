import boto3
from datetime import datetime, timezone

#usern = input("Please Enter a user name: ")


def get_user_age_seconds(username):
    client = boto3.client('iam')
    response = client.get_user(
        UserName=username,
    )

    #print(response)

    now = datetime.now(timezone.utc)

    user_create_date = response['User']['CreateDate']

    #print("User Name:", usern,)
    #print("Creation Date Is: " ,user_create_date,)
    #print("Todays date:" ,now,)
    #print("User ' {} ' is active (seconds):".format(username), (datetime.now(timezone.utc) - user_create_date).total_seconds())


    return print("User ' {} ' is active (seconds):".format(username), (datetime.now(timezone.utc) - user_create_date).total_seconds())

get_user_age_seconds()





