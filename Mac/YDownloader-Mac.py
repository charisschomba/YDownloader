import pafy,sys,getpass
import os,time,subprocess as sub
import pyautogui as py
import pyperclip
import youtube_dl

user = getpass.getuser()

file ='/Users/{}/Downloads/Urls.txt'.format(user)
ulr_list_dir ='/Users/{}/Downloads'.format(user)
if os.path.isfile(file) == True:
    pass
else:
    path="/Users/{}/Downloads".format(user)
    os.chdir(path)
    with open('Urls.txt','w') as file:
        file.write('These are songs downloaded with Y-Downloader\n')

def playlistInfo(url):
    playlist=pafy.get_playlist(url)
    print("Title : " + playlist['title'])
    print("Author: " + playlist['author'])
    print("Items : " + str(len(playlist['items'])))

def mp3(url):
    path="/Users/{}/Downloads/Music".format(user)
    os.chdir(path)
    songs=pafy.new(url)
    song=songs.getbestaudio()
    print (songs.title)
    file=song.download()
    file_split=file.split('.webm')
    renamed = file_split[0] + '.mp3'
    file_path = "/Users/{}/Downloads/Music/{}".format(user,file)
    new_file = "/Users/{}/Downloads/Music/{}".format(user,renamed)
    os.rename(file_path,new_file)
    print('Download Completed ')

def mp4(url):
    path="/Users/{}/Downloads/Video".format(user)
    os.chdir(path)
    songs=pafy.new(url)
    song=songs.getbest(preftype="any")
    print (songs.title)
    file=song.download(quiet=False)
    print('Download Completed ')

def playlist(url):
    plurl = url
    playlist = pafy.get_playlist(url)
    path="/Users/{}/Downloads".format(user) +"/Playlist/{}".format(playlist['title'])
    join_=os.path.join(path)
    file ='/Users{}/Downloads/Playlist'.format(user)
    if  os.path.isdir(file) == True:
        pass
    else:
        os.mkdir(file)
    if  os.path.isdir(path) == True:
        pass
    else:
        dpath=os.mkdir(join_)
    os.chdir(join_)
    playlistInfo(url)
    with youtube_dl.YoutubeDL({}) as ydl:
        ydl.download([url])

def from_text_file():
    os.chdir(ulr_list_dir)
    file = "url_list"
    file = file +'.txt'
    if os.path.isfile(file) == True:
        if os.stat("url_list.txt").st_size == 0:
            print('url_list.txt is empty,please add Audio/Vedio links to continue ')
            print('url_list.txt is in {}'.format(os.getcwd()))
        else:
            print('Downloading Videos from '+ os.path.join(os.getcwd()+'/url_list.txt'))
            with open(file,'r') as urls:
                for link in urls:
                    try:
                        mp4(link)
                    except:
                        print("An error occurred while downloading "+str(link))
            print('Download completed')
def from_text_file_mp3():
    os.chdir(ulr_list_dir)
    file = "url_list"
    file = file +'.txt'
    if os.path.isfile(file) == True:
        if os.stat("url_list.txt").st_size == 0:
            print('url_list.txt is empty,please add Audio/Vedio links to continue ')
            print('url_list.txt is in {}'.format(os.getcwd()))
        else:
            print('Downloading Videos or Audios from '+ os.path.join(os.getcwd()+'/url_list.txt'))
            with open(file,'r') as urls:
                for link in urls:
                    try:
                        mp3(link)
                    except:
                        print("An error occurred while downloading "+str(link))
            print('Download completed')

    elif os.path.isfile(file) == False:
        with open('url_list.txt','w') as file:
            print('Please add download links to '+os.path.join(os.getcwd()+'/url_list.txt') )
    else:
        print('The file passed does not exist the current directory')
        print('Please double check it')

def save_url_(url):
    path="/Users/{}/Downloads".format(user)
    os.chdir(path)
    song=pafy.new(url)
    Title=song.title
    c=open('Urls.txt','r+')
    if Title in c.read():
        pass
    else:
        try:
            c.write(Title + '\n')
            c.write(url + '\n')
            c.close()
        except:
            pass

def saveUrl(url):
    path="/Users/{}/Downloads".format(user)
    os.chdir(path)
    playlist=pafy.get_playlist(url)
    Title=playlist['title']
    c=open('Urls.txt','r+')
    if Title in c.read():
        pass
    else:
        try:
            c.write(Title + '\n')
            c.write(url + '\n')
            c.close()
        except:
            pass

def downloadType():

    type=py.confirm(text='Choose Download Type',buttons=['Audio','Video','Playlist',"From Text File Video","From Text File Audio"])

    if type == "Audio":
        save_url_(url)
        mp3(url)

    elif type == 'Video':
        save_url_(url)
        mp4(url)
    elif type == 'Playlist':
       saveUrl(url)
       playlist(url)
    elif type == "From Text File Video":
        from_text_file()
    elif type == "From Text File Audio":
        from_text_file_mp3()
    else:
        main()

print('-------------------------------------------------------------------------------------------------------')
print('YDownloader')
print('Created by Chariss')
print('Beta Version')
print('--------------------------------------------------------------------------------------------------------')
print(" For automatic Download copy the url or 11 digit youtube video code to clipboard and click Download ")
url =''
def main():
    while True:
        response=py.confirm(text='Download or Exit',buttons=['Download','Exit'])
        if response == 'Download':
            global url
            url=pyperclip.paste() or py.prompt(text="URL",title='Enter Url',default='')
            try:
                downloadType()
            except:
                print('An error occured when processing your download request.')
                print("Please use a Valid URL or Confirm if your clipboard has the correct URL")
                print("Make sure youtube-dl is in Y-Downloader Directory.")
                print('Y-Downloader downloads youtube content only.')

        elif response == 'Exit':
            print('Thanks for using Y Downloader')
            sys.exit()

        else:
            print('You did not Press Download or Exit' )


if __name__ == '__main__':
   main()
