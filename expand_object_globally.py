import json
import logging
import boto3
from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)

filename = 'secret_for_agents.txt'

# I'M BATMANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN

def upload_file(agent_name, bucket):
    """Upload a file to an S3 bucket

    :param agent_name:
    :param bucket: Bucket to upload to
    """

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(filename, bucket, filename)
        logging.info(f'Uploading file to agent {agent_name} has been finished with response: {response}')
    except ClientError as e:
        logging.error(e)


def download_secret_file():
    s3 = boto3.client('s3')
    # TODO change BUCKET_NAME and OBJECT_NAME
    s3.download_file('mytripinitaly', 'secret.txt ', filename)


if __name__ == '__main__':
    download_secret_file()

    with open('agents.json') as json_file:
        agents_bucket = json.load(json_file)

    # TODO use agents_bucket and upload_file to upload file_name to each agent's bucket
