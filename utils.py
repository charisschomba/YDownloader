import pafy
import os
import getpass

user = getpass.getuser()
path = "/Users/{}/Downloads".format(user)

class Helpers:

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
        os.chdir(path)
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


