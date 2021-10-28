import json
import logging
import boto3
from botocore.exceptions import ClientError
#logging as event, Confirmation that things are working as expected
logging.basicConfig(level=logging.INFO)

filename = 'secret_for_agents.txt'


def upload_file(agent_name, bucket):
    """Upload a file to an S3 bucket

    :param agent_name:
    :param bucket: Bucket to upload to
    """

    # Upload the file
    #Create a low-level service client by name using the default session.It allows you to directly create, update, and delete AWS resources from your Python scripts
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(filename, bucket)
        logging.info(f'Uploading file to agent {agent_name} has been finished with response: {response}')
    except ClientError as e:
        logging.error(e)


def download_secret_file():
    s3 = boto3.client('s3')
    s3.download_file('mytripinitaly', 'secret.txt', filename)
    s3.download_file('BUCKET_NAME', 'OBJECT_NAME', filename)


if __name__ == '__main__':
    download_secret_file()

    with open('agents.json') as json_file:
        agents_bucket = json.load(json_file)
    for agent, bkt in agents_bucket.items():
        upload_file(agent, bkt)
    # TODO use agents_bucket and upload_file to upload file_name to each agent's bucket
