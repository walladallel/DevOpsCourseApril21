import json
import logging
import boto3
from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)

file_name = 'secret.txt'


def upload_file(agent_name, bucket):
    """Upload a file to an S3 bucket

    :param agent_name:
    :param bucket: Bucket to upload to
    """

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket)
        logging.info(f'Uploading file to agent {agent_name} has been finished with response: {response}')
    except ClientError as e:
        logging.error(e)


if __name__ == '__main__':
    with open('agents.json') as json_file:
        agents_bucket = json.load(json_file)

    for agent, bkt in agents_bucket.items():
        upload_file(agent, bkt)
