# YDownloader
YDownloader script downloads Youtube contents.
The script downloads Audio,Video and the playlist.

## for windows users,Download use YDownloader.exe

## Requirements

- [Python3](https://www.python.org/) (programming languag)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/)(To isolate script modules)

## How to setup it up:

1.sudo install python3

2.pip install virtualenv

Clone this repository:

git clone  https://github.com/charisschomba/YDownloader.git

cd YDownloader

## Create a virtual environment in the root directory:

virtualenv [name of virtualenv]

## Activate the virtualenv:

source [name of virtualenv]/bin/activate

## On your terminal run:

pip install -r requirements.txt

to install the modules

## On your terminal run:

python YDownloader.py


## How to use it.
You can manually enter the url or copy it and the script detect the copied url.

## The  script has five options
## 1. Audio

Downloads Audio

## 2. Video

Downloads Video

## 3. Playlist

The url must be a playlist url.

## 4. From text file video

This option downloads videos from a text file

## 5. From text file Audio

This option downloads Audio from a text file

## For option 4 and 5

The first you choose option 4 or 5 without url_list in the download folder,
the script will create one for you.

you should have url_list.txt in /home/[user]/Downloads/

for example /home/anonymous/Downloads/url_list.txt with a list of all urls.










