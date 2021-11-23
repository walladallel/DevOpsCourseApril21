import boto3
from datetime import datetime, timezone
from termcolor import colored


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
    print("User ' {} ' is active (seconds):".format(username), (datetime.now(timezone.utc) - user_create_date).total_seconds())

    max_user_age_seconds = (172800.0)

    user_seconds = (datetime.now(timezone.utc) - user_create_date).total_seconds()
    if user_seconds > max_user_age_seconds:

        expired_sub = True
        print("User  ' {} ' is ".format(username),(colored('Expired', 'red')))
        print("--------------------------------------------")


    else:
        expired_sub = False
        print("--------------------------------------------")
    print("Return",expired_sub,user_seconds,max_user_age_seconds)
    return expired_sub

if __name__ == '__main__':
    get_user_age_seconds("test")







