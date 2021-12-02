from youtube_dl import YoutubeDL


def search_download(search_str, search_results):
    """
    This function gets a search string and download the first search_results results
    If you don't want to download the file every run, just to get the result metadata, change below
    download=True to download=False

    :param search_str:
    :param search_results: number of results to download
    :return: a list of downloaded filenames
    """
    with YoutubeDL({'format': 'bestaudio', 'noplaylist': 'True'}) as ydl:
        videos = ydl.extract_info(f"ytsearch{search_results}:{search_str}", download=True)['entries']
        return [ydl.prepare_filename(video) for video in videos]


if __name__ == '__main__':
    # TODO you can change to any search string you want
    downloaded_files = search_download('הגשש', 5)

    # TODO use downloaded_files and complete a few lines to upload them to an S3 bucket
    my changes....

