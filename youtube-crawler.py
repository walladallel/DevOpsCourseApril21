from youtube_dl import YoutubeDL
import json
import logging
import boto3
from botocore.exceptions import ClientError


def search_download(search_str, search_results):
    with YoutubeDL({'format': 'bestaudio', 'noplaylist': 'True'}) as ydl:
        videos = ydl.extract_info(f"ytsearch{search_results}:{search_str}", download=True)['entries']
        return [ydl.prepare_filename(video) for video in videos]


if __name__ == '__main__':
    downloaded_files = search_download('nirvana', 1)
    s3_client = boto3.client('s3')
    s3_client.upload_file('downloaded files', 'eyalyoutube', 'youtube_files')
    
