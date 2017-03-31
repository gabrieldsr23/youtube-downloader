from tkinter import *
from tkinter import messagebox
from download_yt import *
import time

class App(object):
    def __init__(self, master=None):
        self.root = Tk()
        self.root.geometry("400x250")
        self.root.wm_title("Youtube Downloader")
        self.root.configure(background='red')
        label_url = Label (self.root, text= "Enter Url:", background='red')
        label_url.place(x=70, y=20)

        filename = PhotoImage(file='youtube.png')
        self.background_label = Label(self.root, image=filename)
        self.background_label.place(x=80, y=60)
        self.background_label.configure(background='red')

        self.entrytext = StringVar()
        entry_url = Entry(self.root, textvariable=self.entrytext)
        entry_url.place(x=140,y=20)

        self.buttontext = StringVar()
        self.buttontext.set("Baixar MP3")
        self.btt_mp3 = Button(self.root, textvariable=self.buttontext, command=self.clicked_mp3)
        self.btt_mp3.place(x=70, y=60)

        self.buttontext = StringVar()
        self.buttontext.set("Baixar MP4")
        self.btt_mp4 = Button(self.root, textvariable=self.buttontext, command=self.clicked_mp4)
        self.btt_mp4.place(x=215, y=60)

        self.buttontext = StringVar()
        self.buttontext.set(" Exit ")
        self.btt_exit = Button(self.root, textvariable=self.buttontext, command=self.quit).place(x=160, y=100)

        self.label_downloading = Label(self.root, text='', background='red')
        self.label_downloading.place(x=120,y=0)

        self.root.mainloop()

    def quit(self):
        exit()

    def clicked_mp3(self):
        url = self.entrytext.get()
        download_mp3(url)
        self.label_downloading.config(text='Music Downloaded !!')

    def clicked_mp4(self):
        url = self.entrytext.get()
        download_mp4(url)
        self.label_downloading.config(text='Video Downloaded !!')


App()
