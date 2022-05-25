from genericpath import exists
from pytube import YouTube
import os.path
yt = YouTube(str(input("Enter URL of youtube video: \n ")))
video = yt.streams.filter(only_audio=True).first()
destination = ''
out_file = video.download(output_path=destination)