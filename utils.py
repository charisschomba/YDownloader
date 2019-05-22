import pafy
import os
import getpass
import platform


user = getpass.getuser()


class Helpers:

    @staticmethod
    def check_platform(file=''):
        os_platform = platform.system()
        if os_platform == 'Windows' or os_platform == 'Darwin':
            return "/Users/{}/Downloads/{}".format(user, file)
        elif os_platform == 'Linux':
            return "/home/{}/Downloads/{}".format(user, file)

    @staticmethod
    def create_urls_file():
        file = Helpers.check_platform('Urls.txt')
        if os.path.isfile(file) == True:
            pass
        else:
            path = Helpers.check_platform()
            os.chdir(path)
            with open('Urls.txt', 'w') as file:
                file.write('These are songs downloaded with Y-Downloader\n')

    @staticmethod
    def ydl_options():
        return {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

    @staticmethod
    def save_url_(url):
        Helpers.create_urls_file()
        song = pafy.new(url)
        Title = song.title
        os.chdir(Helpers.check_platform())
        c = open('Urls.txt', 'r+')
        if Title in c.read():
            pass
        else:
            try:
                c.write(Title + '\n')
                c.write(url + '\n')
                c.close()
            except:
                pass

    @staticmethod
    def save_url(url):
        Helpers.create_urls_file()
        os.chdir(Helpers.check_platform())
        playlist = pafy.get_playlist(url)
        Title = playlist['title']
        c = open('Urls.txt', 'r+')
        if Title in c.read():
            pass
        else:
            try:
                c.write(Title + '\n')
                c.write(url + '\n')
                c.close()
            except:
                pass

    @staticmethod
    def playlist_info(url):
        playlist = pafy.get_playlist(url)
        print("Title : " + playlist['title'])
        print("Author: " + playlist['author'])
        print("Items : " + str(len(playlist['items'])))

