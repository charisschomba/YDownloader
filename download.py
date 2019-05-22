import sys
import pyperclip
from termcolor import colored
from music import Music
from utils import Helpers

Audio = Music()
Helper = Helpers()


def download_type():

    music_type = input(colored('Press A for Audio  V for Video P for Playlist : > ', 'green'))
    print(colored('processing you download request ...........', 'blue'))

    if music_type == "A" or music_type == "a":
        Helpers.save_url_(url)
        Audio.mp3(url)

    elif music_type == 'V' or music_type == 'v':
        Helpers.save_url_(url)
        Audio.mp4(url)

    elif music_type == 'P' or music_type == 'p':
        Helpers.save_url(url)
        Audio.playlist(url)
    else:
        main()


print(colored('---------------------------------------------------------------------------------------', 'blue'))
print(colored('YDownloader', 'blue'))
print(colored("Copy youtube url to the clipboard and click D to Download ", 'blue'))
print(colored('---------------------------------------------------------------------------------------', 'blue'))

url = ""


def main():
    while True:
        response = input(colored('Press D to Download or Q to Quit: > ', 'green'))
        if response == 'd' or response == 'd':
            global url
            url = pyperclip.paste()
            try:
                download_type()
            except:
                print(colored('An error occurred when processing your download request.', 'red'))
                print(colored("Please use a Valid URL or Confirm if your clipboard has the correct URL", 'red'))
                print(colored('Y-Downloader downloads youtube content only.', 'red'))

        elif response == 'Q' or response == 'q':
            print(colored('Thanks for using Y Downloader', 'blue'))
            sys.exit()

        else:
            print(colored('You did not Press D or Q', 'red'))


if __name__ == '__main__':
    main()
