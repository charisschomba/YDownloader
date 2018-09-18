# YDownloader
YDownloader script downloads Youtube contents.
The script downloads Audio,Video and the playlist.

## For windows users,download YDownloader.exe

# YDownloader
YDownloader script downloads Youtube contents.
The script downloads Audio,Video and the playlist.

## For Mac and Linux Users

## Requirements

- [Python3](https://www.python.org/) (programming languag)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/)(To isolate script modules)

## How to setup it up:

1.sudo install python3

2.pip install virtualenv

Clone this repository:

git clone  https://github.com/charisschomba/YDownloader.git

for linux cd YDownloader,
or
for mac users cd YDownloader/Mac 


## Create a virtual environment in the root directory using python3:

virtualenv -p pytho3 [name of virtualenv]

## Activate the virtualenv:

source [name of virtualenv]/bin/activate

## On your terminal run:

pip3 install -r requirements.txt

to install the libraries required

### Update youtube-dl by running 

pip3 install --upgrade youtube-dl


## if you get certificate errors run the following command to update them(Mac users)
/Applications/Python\"python version"/Install\ Certificates.command

User your current python version

for example,if you have python 3.6

`/Applications/Python\ 3.6/Install\ Certificates.command`

## On your terminal run:

python YDownloader-Linux.py if your using linux

or

python YDownloader-Mac.py if your using MacOs


## How to use it.
You can manually enter the url or copy it and the script detect the copied url.

## The  script has five options
## 1. Audio

Downloads Audio
First create a Music folder in Downloads
Downloads/Music

## 2. Video

Downloads Video
First create a Video folder in Downloads
Downloads/Video

## 3. Playlist

The url must be a playlist url.
First create a Playlist folder in Downloads
Downloads/Playlist

## 4. From text file video

This option downloads videos from a text file

## 5. From text file Audio

This option downloads Audio from a text file

## For option 4 and 5

The first you choose option 4 or 5 without url_list in the download folder,
the script will create one for you.

you should have url_list.txt in the /Downloads/ folder with a list of urls,each url should in a new line.

for example /home/anonymous/Downloads/url_list.txt with a list of all urls.

## if you get certificate errors run the following command to update them(Mac users)
/Applications/Python\"python version"/Install\ Certificates.command

User your current python version

for example,if you have python 3.6

`/Applications/Python\ 3.6/Install\ Certificates.command`
## if you get signiture varification failed error

run this command to update youtube-dl

`sudo -H pip3 install --upgrade youtube-dl`

















