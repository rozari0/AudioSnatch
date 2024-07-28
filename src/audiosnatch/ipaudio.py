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
    "goldenaudiobooks",  # https://goldenaudiobooks.club/
    "sharedaudiobooks",  # https://sharedaudiobooks.net/
    "hdaudiobooks",  # https://hdaudiobooks.ne
    "findaudiobook",  # https://findaudiobook.club/
    "bagofaudio",  # https://bagofaudio.com/
    "bigaudiobooks",  # https://bigaudiobooks.club/
    "fulllengthaudiobooks",  # https://fulllengthaudiobooks.net/
    "primeaudiobooks",  # https://primeaudiobooks.club/
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
        if not path.exists(down_obj.get_dest()):
            down_obj.start()
        else:
            print(f"\t{down_obj.get_dest()} already exists. Skipping this file.")
    print("Completed")
