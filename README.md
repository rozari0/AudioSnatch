
# Audio Snatch

This Python cli tool allows you to download audiobooks from multiple websites.

## Table of contents
- [Supported Websites](#supported-websites)
- [Installation](#installation)
- [Usage/Examples](#usageexamples)
- [Acknowledgements](#acknowledgements)


## Supported Websites

- [Golden Audiobooks](https://goldenaudiobooks.club/)
- [Shared Audiobooks](https://sharedaudiobooks.net/)
- [HD Audiobooks](https://hdaudiobooks.net/)
- [Find Audiobook](https://findaudiobook.club/)
- [Bag of Audio](https://bagofaudio.com/)
- [Big Audiobooks](https://bigaudiobooks.club/)
- [Full Length Audiobooks](https://fulllengthaudiobooks.net/)
- [Prime Audiobooks](https://primeaudiobooks.club/)

## Installation

To install this project on your machine, you can use one of the following methods:

### Recommended: Using pipx

```bash
pipx install audiosnatch
```
### Using pip

```bash
pip install audiosnatch
```

### To get the latest: From the repository 

```bash
pip install git+https://github.com/rozari0/AudioSnatch.git
```
## Usage/Examples

### Download in current folder


```bash
audiosnatch https://sharedaudiobooks.net/george-orwell-animal-farm-audiobook/
```

### Download in Another folder
```bash
audiosnatch -O ~/Music https://sharedaudiobooks.net/george-orwell-animal-farm-audiobook/
```
## Acknowledgements

 - [pySmartDL](https://github.com/iTaybb/pySmartDL)
 - [Rich Click](https://github.com/ewels/rich-click)
