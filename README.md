# YDownloader
YDownloader script downloads Youtube contents.
The script downloads Audio, Videos and Playlists.

## Requirements

- [Python3](https://www.python.org/)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/)
- [Homebrew](https://brew.sh/)
- [chocolately](https://chocolatey.org) - windows users

## How to setup it up:

1.Install [Python3](https://www.python.org/)

##### Install virtualenv

2.`pip install virtualenv`

##### Clone this repository:

`git clone  https://github.com/charisschomba/YDownloader.git`

##### Install audio converter dependencies depending on your operating system

`brew install ffmpeg` for MacOs

`sudo apt-get install ffmpeg` or `sudo apt-get install -y libav-tools` for Linux

##### For windows users

Run `CMD` as administrator and paste the code below to install chocolatey

`@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"`

Once the  installation is complete run `choco install ffmpeg` to install `ffmpeg`

`cd YDownloader`
##### Create a virtual environment in the root directory using python3:

`virtualenv -p python3 yd`

##### Activate the virtualenv:

`source yd/bin/activate` - for MacOs and Linux

`Yd\Scripts\activate` - for windows users

##### On your terminal run:

`pip3 install -r requirements.txt` - to install the packages required
##### Update youtube-dl by running 

`pip3 install --upgrade youtube-dl`

##### On your terminal run:

`python download.py` and type `D` to download or `Q` to quit.


### How to use it.
##### This script downloads only Youtube contents.
- Copy `audio/video/playlist url` and start the script.

- Eg playlist url - `https://www.youtube.com/watch?v=aJOTlE1K90k&list=PLuUrokoVSxlcgocBXbDF76yWd3YKWpOH9` 
- Audio /Video url - `https://www.youtube.com/watch?v=dmJefsOErr0`

- Choose type `A` for Audio `V` for Video or `P` for Playlist to download.
- Note: This script will only download playlist if the url is a playlist url.
- Choose `Playlist option` if the url is a valid youtube playlist url.



