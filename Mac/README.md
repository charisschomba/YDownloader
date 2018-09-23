# YDownloader
YDownloader script downloads Youtube contents.
The script downloads Audio,Video and the playlist.

## Requirements

- [Python3](https://www.python.org/) (programming languag)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/)(To isolate script modules)
- [Homebrew](https://brew.sh/)

## How to setup it up:

1.sudo install python3

2.pip install virtualenv

Clone this repository:

git clone  https://github.com/charisschomba/YDownloader.git

brew install libav 

cd YDownloader/Mac

## Create a virtual environment in the root directory using python3:

virtualenv -p pytho3 yd

## Activate the virtualenv:

source yd/bin/activate

## On your terminal run:

pip3 install -r requirements.txt

to install the libraries required

### Update youtube-dl by running 

pip3 install --upgrade youtube-dl

## Create this folders in Downloads Directory.

Music
Video
Playlist

## On your terminal run:

python YDownloader-Mac.py if your using MacOs


## How to use it.
You can manually enter the url or copy the url and the script detect the copied url.

eg https://www.youtube.com/watch?v=-5S0NOlIxTk 

click download and select an option

## The  script has five options
## 1. Audio

Downloads Audios

## 2. Video

Downloads Videos

## 3. Playlist

The url must be a playlist url.

## 4. From text file video

This option downloads videos from a text file

## 5. From text file Audio

This option downloads Audio from a text file

## For option 4 and 5

If first you choose option 4 or 5 without url_list in the Downloads folder,
the script will create one for you.

you should have url_list.txt in the /Downloads/ folder with a list of urls,each url should in a new line.

for example /home/anonymous/Downloads/url_list.txt with a list of all urls.



















