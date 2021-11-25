import boto3
from botocore.exceptions import ClientError
from get_user_age_seconds import get_user_age_seconds
from termcolor import colored
client = boto3.client('iam')

# Admin UserName To be ignored
admin = "noamsint"


def delete_outdated_usernames():

    # Deletes users older than max_user_age_seconds

    while True:
                client = boto3.client('iam')

                iam = boto3.resource('iam')

                policy = iam.Policy('arn:aws:iam::955114013936:policy/S3VideoReader')
                response = client.list_users()


                users_d = (response['Users'])
               # print(users_d)

                for x in range(len(users_d)):
                    fo_user = users_d[x]['UserName']
                    expired = get_user_age_seconds(fo_user)
                    if expired == True and fo_user != admin:

                        try:
                            print("Trying To Detach User '{} ' From Policy...".format(fo_user))
                            print("--------------------------------------------")
                            response_policy = policy.detach_user(
                                UserName=fo_user)
                            
                        except client.exceptions.NoSuchEntityException :
                            print('Policy Was Not Found')
                            print("--------------------------------------------")

                            continue

                        """
                        try:
                            print("Trying to Delete Access Key")
                            response_del_acc = client.delete_access_key(
                            AccessKeyId='AKIA54YJ3ITYDA3JMFOU',
                            UserName=fo_user,)
                            print(response_del_acc)
                        except ClientError as e:
                            print("Unexpected error: %s" % e)
                        """

                        try:
                            print((colored("Trying To Delete User '{}'...".format(fo_user), 'Yellow')))
                            print("--------------------------------------------")
                            response_del = client.delete_user(
                                UserName=fo_user
                            )
                            #print(response_del)
                            print((colored("Deleted Successfully '{}'".format(fo_user), 'green')))
                            print("--------------------------------------------")
                        except ClientError as e:
                            print("Unexpected error: %s" % e)



                        print("Getting users from IAM...")
                        response = client.list_users()
                        users_list = (response['Users'])
                        print(users_list)

delete_outdated_usernames()



