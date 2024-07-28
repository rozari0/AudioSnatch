from os import getcwd

import rich_click as click
from rich import print
from validators.url import url as url_validator

from audiosnatch import ipaudio


@click.command()
@click.option(
    "--output",
    "-O",
    type=click.Path(),
    default=getcwd(),
    help="Output path. [Default '.']",
)
@click.argument("url", nargs=-1)
def download(url, output):
    """Download AudioBook From goldenaudiobooks

    Usage: audiosnatch download <options> <url(s)>
    """
    urls = []
    for U in url:
        if U not in urls and url_validator(U):
            urls.append(U)

    for url in urls:
        if any(website in url for website in ipaudio.website_lists):
            ipaudio.download_now(**ipaudio.gererate_list(url), basepath=output)
        else:
            print(f"{url} isn't implemented yet!")


@click.command()
@click.argument("search_term", nargs=-1)
def search(search_term):
    """Search AudioBook

    Usage: audiosnatch search <options> <search term>
    """
    print(f"Searched for {' '.join(search_term)}")


@click.group()
def main() -> None:
    pass


main.add_command(download)
main.add_command(search)
