import youtube_dl
import os
import getpass
import pafy
from termcolor import colored
from utils import Helpers

user = getpass.getuser()
utils = Helpers()


class Music:

    @staticmethod
    def create_path(path):
        if not os.path.exists(path):
            os.mkdir(path)
            os.chdir(path)
        os.chdir(path)

    def mp3(self, url):
        path = Helpers.check_platform('Music')
        self.create_path(path)
        ydl_opts = utils.ydl_options()
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(colored('Download Completed', 'green'))

    def mp4(self, url):
        path = Helpers.check_platform('Videos')
        self.create_path(path)
        try:
            with youtube_dl.YoutubeDL({}) as ydl:
                ydl.download([url])
            print(colored('Download Completed', 'green'))
        except:
            print(colored('something went wrong try again', 'red'))

    def playlist(self, url):
        playlist = pafy.get_playlist(url)
        path = Helpers.check_platform() + "/Playlists/{}".format(playlist['title'])
        join_ = os.path.join(path)
        file = Helpers.check_platform('Playlists')
        if os.path.isdir(file) == True:
            pass
        else:
            os.mkdir(file)
        if os.path.isdir(path) == True:
            pass
        else:
            os.mkdir(join_)
        os.chdir(join_)
        utils.playlist_info(url)
        with youtube_dl.YoutubeDL({}) as ydl:
            ydl.download([url])

