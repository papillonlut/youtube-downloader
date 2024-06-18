from pytube import YouTube
from tkinter import *
from tkinter import Tk
import os
import time
import customtkinter

def newWindow():
    url = url_entry.get()
    if url:
        YouTube(url).streams.first().download("ytb-downloader")

root = Tk()
root.title("YouTube Downloader")
root.geometry("300x100")
root.maxsize(300,100)
root.minsize(300,100)

url_label = Label(root, text="Enter YouTube URL:")
url_label.pack()

url_entry = Entry(root, width=40)
url_entry.pack()

b1 = Button(root, text = "Download", command= newWindow)
b1.pack()

root.mainloop()
