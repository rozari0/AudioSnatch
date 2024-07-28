"""
IP Audio is a website that hosts audio for goldenaudiobooks.club, sharedaudiobooks.net,hdaudiobooks.net
"""

from os import mkdir, path
from urllib import parse

from bs4 import BeautifulSoup
from pySmartDL import SmartDL
from requests import get
from rich import print

website_lists = [
    "goldenaudiobooks", # 
    "sharedaudiobooks",
    "hdaudiobooks",
    "findaudiobook",
    "bagofaudio",
    "bigaudiobooks",
    "fulllengthaudiobooks",
    "primeaudiobooks",
]


def gererate_list(url):
    response = get(url)
    soup = BeautifulSoup(response.text, "lxml")

    title = soup.head.title.text.strip()
    audios = soup.find_all("audio", class_="wp-audio-shortcode")
    audios = list(map(lambda audio: audio.source.get("src"), audios))

    return {"title": title, "audios": audios}


def download_now(title, audios, basepath):
    print(f"Downloading [bold]{title}[/bold]")
    for audio in audios:
        bookpath = path.join(basepath, parse.unquote(audio.split("/")[-2]))
        print(f"\tFile: {bookpath}/{audio.split('/')[-1].split('?')[0]}")
        if not path.exists(bookpath):
            mkdir(bookpath)
        down_obj = SmartDL(audio, bookpath)
        down_obj.start()
    print("Completed")
