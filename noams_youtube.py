from youtube_dl import YoutubeDL
import boto3
from termcolor import colored
s3_client = boto3.client('s3')

def search_download(search_str, search_results, username):


    with YoutubeDL({'format': 'bestaudio', 'noplaylist': 'True', }) as ydl:
        videos = ydl.extract_info(f"ytsearch{search_results}:{search_str}", download=True)['entries']
        return [ydl.prepare_filename(video) for video in videos],

if __name__ == 'USER INTERFACE':
    downloaded_files = search_download(search_str,search_results,username)

    try:
        for a in downloaded_files:
            try:
                s3_client.upload_file(a, 'youtube-crawler-bucket', username + "/" + a)
                print((colored("Successfully Downloaded {} ".format(a), 'green')))
            except Exception as g:
                print("Error", g)
                exit(1)

    except Exception as e:
        print("Error", e)
        exit(1)
