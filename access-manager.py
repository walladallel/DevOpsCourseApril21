import boto3
from botocore.exceptions import ClientError


def create_user(username):
    """
    Create a user "username" with an appropriate permissions (S3VideoReader you've just created)
    """
    try:
        pass  # TODO your code here
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print("User already exists")
        else:
            print("Unexpected error: %s" % e)


def delete_outdated_usernames(max_user_age_seconds):
    """
    Deletes users older than max_user_age_seconds
    """
    # TODO List all users
    # TODO Iterate over the users in "for" loop
    # TODO Inside the loop, use "get_user_age_seconds" from utils.py to check if the user is older than max_user_age_seconds
    # TODO Delete the user if his age is greater than max_user_age_seconds
    pass


if __name__ == '__main__':

    iam_client = boto3.client('iam')

    # create_user('john')
    # delete_outdated_usernames(60)
