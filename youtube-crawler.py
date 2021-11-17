from youtube_dl import YoutubeDL
import json
import logging
import boto3
from botocore.exceptions import ClientError


def search_download(search_str, search_results):
    """
    This function gets a search string and download the first search_results results
    If you don't want to download the file every run, just to get the result metadata, change below
    download=True to download=False

    :param search_str:
    :param search_results: number of results to download
    :return: a list of downloaded filenames
    """
    with YoutubeDL({'format': 'bestaudio', 'noplaylist': 'False'}) as ydl:
        videos = ydl.extract_info(f"ytsearch{search_results}:{search_str}", download=True)['entries']
        return [ydl.prepare_filename(video) for video in videos]


if __name__ == '__main__':
   downloaded_files = search_download('nirvana', 1)

    # TODO use downloaded_files and complete a few lines to upload them to an S3 bucket
s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file({'format': 'bestaudio', 'noplaylist': 'False'})
        logging.info(f'Uploading file to agent {'format': 'bestaudio', 'noplaylist': 'False'} has been finished with response: {response}')
    except ClientError as e:
        logging.error(e)
