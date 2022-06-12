from msilib.schema import File
import os
from Media import Clip, Documentary, Series, Film
from Actor import Actor
from pytube import YouTube

movies = []
actors = []
def clear_console():
    clear = lambda: os.system('cls')
    clear()

def download():
    clear_console()
    print("=== DOWNLOAD ===")
    name = input('Enter movie name')
    media = next((media for media in movies if name in media.name), None)
    url = media.url
    yt = YouTube(url)
    mp4_files = yt.streams.filter(file_extension="mp4")
    mp4_369p_files = mp4_files.get_by_resolution("360p")
    mp4_369p_files.download("/downloads")

def load_from_db():
    global movies,actors
    movies = []
    actores = []
    data_media = open('media.txt','r')
    data_actors = open('actors.txt','r')
    actors_list = data_actors.read().split("\n")

    for i in range(1, len(actors_list)):
        info = actors_list[i].split(",")
        id, name, age, media_id = int(info[0]), info[1], int(info[2]), int(info[3])
        actor = Actor(name, age, media_id)
        actors.append(actor)
    data_actors.close()

    media_list = data_media.read().split("\n")
    for i in range(1, len(media_list)):
        info = media_list[i].split(",")
        
        id, type, genre, name, director, score, url, duration, parts =\
             int(info[0]),info[1],info[2],info[3],info[4],int(info[5]),info[6],int(info[7]), int(info[8])

        media_actors = []
        for actor in actors:
            if actor.media_id == id:
                media_actors.append(actor)
        media = None
        if(type == 'film'):
            media = Film(id, name, director,score, duration,media_actors,url)
        elif(type == 'series'):
            media = Series(id, name, director,score,media_actors,url, parts )
        elif(type == 'clip'):
            media = Clip(id, name, director,score,duration,media_actors,url )
        else:
            media = Documentary(id, name, director,score,duration,media_actors,url)
        movies.append(media)
    data_media.close()

def showMenu():
    print("1- Add Movie")
    print("2- Edit Movie")
    print("3- Delete Movie")
    print("4- Search")
    print("5- Show List")
    print("6- Exit")


def show_list():
    clear_console()
    print("=== MEDIA LIST ===")
    for movie in movies:
        movie.show_info()
    input('press any key to back')

def delete_movie():
    clear_console()
    print("=== DELETE MEDIA ===")
    name = input('enter name: ')
    deleted = True
    while(deleted):
        for i in range(len(movies)):
            if(name in movies[i].name):
                del movies[i]
                break
            deleted = False
    input('sucessfully removed. press any key to back ...')

def add_movie():
    clear_console()
    print("=== ADD NEW MEDIA ===")
    type = int(input("type: 1-clip 2-documentary 3-series 4-film: "))

    id = movies[len(movies)-1].id + 1
    genre = input("genre: ")
    name = input("name: ")
    director = input("director: ")
    score = int(input("score: "))
    url = input("url: ")
    duration = int(input("duration: "))

    if(type == 1):
        new_media = Clip(id, name, director,score,duration,[],url )
        type = 'clip'
    elif(type == 2):
        new_media = Documentary(id, name, director,score,duration,[],url)
        type = 'documentary'
    elif(type == 3):
        parts = int(input("parts: "))
        new_media = Series(id, name, director,score,[],url, parts )
        type = 'series'
    else:
        new_media = Film(id, name, director,score, duration,[],url)
        type = 'film'
    if(type == 'film'):
        genre = new_media.genre
    else:
        genre = ''

    if(type == 'series'):
        parts = new_media.parts
    else:
        parts = 0
    
    movies.append(new_media)
    file = open('media.txt', 'a')
    file.write(str(new_media.id) + "," + type+ "," +genre+ "," +new_media.name+ "," +new_media.director+ "," +str(new_media.score)+ "," +new_media.url+ "," +str(new_media.duration)+ "," +str(parts))
    input('sucessfully added. press any key to back ...')

def search_movie():
    clear_console()
    print("=== SEARCH MEDIA ===")
    type = int(input("search by: 1-name 2-time: "))
    if(type == 1):
        name = input('Enter movie name: ')
        for media in movies:
            if(name in media.name):
                media.show_info()
    else:
        sd = int(input('Enter start duration: '))
        ed = int(input('Enter end duration: '))
        for media in movies:
            if(hasattr(media, 'duration') and media.duration >= sd and media.duration <= ed):
                media.show_info()
    
    input('press any key to back ...')
    
def edit_movie():
    clear_console()
    print("=== EDIT MEDIA ===")
    id = int(input('Enter media id: '))
    index = next((index for (index, media) in enumerate(movies) if media.id == id), -1)
    if(index == -1):
        input('not found. press any key to back ...')
        return
    media = movies[index]
    media.show_info()
    newId = int(input('New id (-1 means same id): '))
    if(newId != -1):
        movies[index].id = newId
    newName =input('New name (Enter means same name): ')
    if(newName != ""):
        movies[index].name = newName
    newScore =float(input('New score (-1 means same score): '))
    if(newScore != -1):
        movies[index].score = newScore
    input('sucessfully edited. press any key to back ...')

load_from_db()
choice = -1
while(choice != 6):
    clear_console()
    showMenu()
    choice = int(input())
    if(choice == 1):
        add_movie()
    elif(choice == 2):
        edit_movie()
    elif(choice == 3):
        delete_movie()
    elif(choice == 4):
        search_movie()
    elif(choice == 5):
        show_list()



