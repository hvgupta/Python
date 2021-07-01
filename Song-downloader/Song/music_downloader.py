from youtubesearchpython import VideosSearch
import pafy

def list_reader(filename):
    file = open(filename) 
    line = file.readlines()
    for i in line:
        i = i.rstrip()
        search_song(i)

def search_song(user_input):

    search_= VideosSearch(str(user_input), limit= 1)
    url = ((search_.result())["result"][-1])["link"]
    download_music(url)
    
def download_music(url):
    video_link = pafy.new(url)
    best_quality_audio = video_link.getbestaudio(preftype="m4a")
    temp = True
    while temp:
        try:
            best_quality_audio.download()
            temp = False
            break
        except:
            continue 
    name = video_link.title

if input("Do you want to input a file which all the songs, answer as Yes or no\n").title() == "Yes":
    print("please input the file name, make sure it is a text file (has a .txt ending)")
    user_input = input("State the name of the file, to get better results the songs should be formated like 'artist-song name'\n")
    list_reader(user_input)
elif input("Do you want to type out 1 song at a time individually?, answer as Yes or no\n"):
    user_input = input("state the name of the song, format should be 'artist-song name'\n")
    search_song(user_input)