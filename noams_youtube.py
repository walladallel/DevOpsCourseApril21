from youtube_dl import YoutubeDL
import boto3
"""
username = "Noamss"
search_str ="15 sec video"
search_results="1"
"""
def search_download(search_str, search_results ,username):

    """
    This function gets a search string and download the first search_results results
    If you don't want to download the file every run, just to get the result metadata, change below
    download=True to download=False

    :param search_str:
    :param search_results: number of results to download
    :return: a list of downloaded filenames
    """
    with YoutubeDL({ 'format': 'bestaudio', 'noplaylist': 'True' ,}) as ydl:
        videos = ydl.extract_info(f"ytsearch{search_results}:{search_str}", download=True)['entries']
        return [ydl.prepare_filename(video) for video in videos]



if __name__ == '__main__':
    # TODO you can change to any search string you want
    try:
        downloaded_files = search_download(search_str,search_results,username)

    except Exception as e:
        print("Error", e)
        exit(1)


    s3_client = boto3.client('s3')
    for a in downloaded_files:
        try:
            s3_client.upload_file(a, 'youtube-crawler-bucket',username+"/"+a)
        except Exception as g:
           print("Error" , g)



