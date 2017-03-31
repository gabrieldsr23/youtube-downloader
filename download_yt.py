from __future__ import unicode_literals
import youtube_dl

def download_mp3(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_mp4(url):
    ydl_opts = {}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

