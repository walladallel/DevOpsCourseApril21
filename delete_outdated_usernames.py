import boto3
from botocore.exceptions import ClientError
from get_user_age_seconds import get_user_age_seconds
client = boto3.client('iam')



def delete_outdated_usernames(client):
    """
    Deletes users older than max_user_age_seconds
    """
    response = client.list_users()

    # TODO Iterate over the users in "for" loop

    users_d = (response['Users'])
   # print(users_d)

    for x in range(len(users_d)):
        fo_user = (users_d[x]['UserName'])
        #print(fo_user)
        get_user_age_seconds(fo_user)






    # TODO Inside the loop, use "get_user_age_seconds" from utils.py to check if the user is older than max_user_age_seconds
    # TODO Delete the user if his age is greater than max_user_age_seconds


delete_outdated_usernames(client)



