from bs4 import BeautifulSoup
from requests import get


def get_link(url):
    response = get(url)
    bs = BeautifulSoup(response.text, "lxml")
    title = bs.head.text

    print(title.strip())
    # print(url)


get_link(
    "https://goldenaudiobooks.club/george-orwell-animal-farm-audiobook-stephen-fry/"
)
