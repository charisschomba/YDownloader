import youtube_dl
import os
import getpass
from termcolor import colored

user = getpass.getuser()
from utils import Helpers

utils = Helpers()


class Music:

    @staticmethod
    def create_path(path):
        if not os.path.exists(path):
            os.mkdir(path)
            os.chdir(path)
        os.chdir(path)

    def mp3(self, url):
        path = "/Users/{}/Downloads/Music".format(user)
        self.create_path(path)
        ydl_opts = utils.ydl_options()
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(colored('Download Completed', 'green'))

    def mp4(self, url):
        path = "/Users/{}/Downloads/Video".format(user)
        self.create_path(path)
        try:
            with youtube_dl.YoutubeDL({}) as ydl:
                ydl.download([url])
            print(colored('Download Completed', 'green'))
        except:
            print(colored('something went wrong try again', 'red'))

