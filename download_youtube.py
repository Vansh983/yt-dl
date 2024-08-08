from pytubefix import YouTube
from pytubefix.cli import on_progress

# Example usage
if __name__ == "__main__":
    url = "video_url"

    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)

    ys = yt.streams.get_highest_resolution()
    ys.download()
