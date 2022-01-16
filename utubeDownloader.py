<<<<<<< HEAD
from pytube import YouTube

print("+++++++++++++++++++++___________+++++++++++++++++++++++++")
print("________ !!!!!! YOUTUBE mp3/mp4 DOWNLOADER !!!!!!________")
print("---------------------------------------------------------")
print("1. mp3 download\n2. mp4 download\nEnter your choice>> ")
n = int(input())

try:
    video = YouTube(input("Enter the url>> "))
    path = input("Enter the path for download>> ")

    if(n==1):
        print("Downloading..........")
        mp3 = video.streams.filter(only_audio=True)
        yt1 = mp3.get_highest_resolution().download(path)

    if(n==2):
        print("Downloading..........")
        mp4 = video.streams.filter(file_extension ="mp4")
        yt = mp4.get_highest_resolution().download(path)


    print("Downloaded successfully")

except ConnectionError:
=======
from pytube import YouTube

print("+++++++++++++++++++++___________+++++++++++++++++++++++++")
print("________ !!!!!! YOUTUBE mp3/mp4 DOWNLOADER !!!!!!________")
print("---------------------------------------------------------")
print("1. mp3 download\n2. mp4 download\nEnter your choice>> ")
n = int(input())

try:
    video = YouTube(input("Enter the url>> "))
    path = input("Enter the path for download>> ")

    if(n==1):
        print("Downloading..........")
        mp3 = video.streams.filter(only_audio=True)
        yt1 = mp3.get_highest_resolution().download(path)

    if(n==2):
        print("Downloading..........")
        mp4 = video.streams.filter(file_extension ="mp4")
        yt = mp4.get_highest_resolution().download(path)


    print("Downloaded successfully")

except ConnectionError:
>>>>>>> 5de567f... Utube downloader updated
    print("Connection Error!@$@(#*$")