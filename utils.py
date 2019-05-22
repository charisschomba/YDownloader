import pafy
import os
import getpass

user = getpass.getuser()
path = "/Users/{}/Downloads".format(user)

class Helpers:

    @staticmethod
    def create_urls_file():
        file = '/Users/{}/Downloads/Urls.txt'.format(user)
        if os.path.isfile(file) == True:
            pass
        else:
            path = "/Users/{}/Downloads".format(user)
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
        os.chdir(path)
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

