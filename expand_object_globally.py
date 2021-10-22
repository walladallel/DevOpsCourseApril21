import json
import logging
import boto3
from botocore.exceptions import ClientError
import os

logging.basicConfig(level=logging.INFO)

file_name = 'secret.txt'


def upload_file(agent_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param agent_name:
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        logging.info(f'Uploading file to agent {agent_name} has been finished with response: {response}')
    except ClientError as e:
        logging.error(e)
        return False


if __name__ == '__main__':
    with open('agents.json') as json_file:
        agents_bucket = json.load(json_file)

    # TODO use agents_bucket and upload_file to upload file_name to each agent's bucket
