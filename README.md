# YDownloader
YDownloader script downloads Youtube contents.
The script downloads Audio and Video.

## Requirements

- [Python3](https://www.python.org/) (programming languag)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/)(To isolate script modules)
- [Homebrew](https://brew.sh/)

## How to setup it up:

1.sudo install python3

2.pip install virtualenv

Clone this repository:

`git clone  https://github.com/charisschomba/YDownloader.git`

`brew install libav` 

cd YDownloader

## Create a virtual environment in the root directory using python3:

`virtualenv -p python3 yd`

## Activate the virtualenv:

`source yd/bin/activate`

## On your terminal run:

`pip3 install -r requirements.txt`

to install the libraries required

### Update youtube-dl by running 

pip3 install --upgrade youtube-dl

## On your terminal run:

`python download.py`


## How to use it.
You can manually enter the url or copy the url and the script detect the copied url.

eg https://www.youtube.com/watch?v=-5S0NOlIxTk 

click download and select an option

## The  script has two options
## 1. Audio

Downloads Audios

## 2. Video

Downloads Videos



















