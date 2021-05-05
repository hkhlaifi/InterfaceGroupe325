# Import needed packages
#-*- coding: utf-8 -*-
# For python 2
from tkinter import *
import tkinter as tk
import webbrowser
from PIL import Image, ImageTk
import PIL.Image
import PIL.ImageTk
from tkinter import ttk
import tkinter.font as TkFont
import webbrowser as wb
from queue import Queue
import threading
import sys
from youtubesearchpython import VideosSearch
import pytube
import os
from tkinter import messagebox
# For python 3
try:
    import Tkinter as tk
    import ttk
    from tkFileDialog import askopenfilename
    import tkMessageBox
    import tkSimpleDialog
    from tkSimpleDialog import Dialog
except ModuleNotFoundError:
    import tkinter as tk
    from tkinter import ttk
    from tkinter.filedialog import askopenfilename
    import tkinter.messagebox as tkMessageBox
    import tkinter.simpledialog as tkSimpleDialog
    from tkinter.simpledialog import Dialog
    import numpy as np
    import cv2
##########################################################################

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):       
        tk.Tk.__init__(self, *args, **kwargs)
        # Icon-photo of the window
        self.iconphoto(False, tk.PhotoImage(file='images/paon.png'))
        # window configuration
        self.geometry("250x150+300+300")
        self.configure(background="grey")
        # window titre
        self.title("Interface recherche vidéo amateurs")
        # Interface geometry
        self.geometry("1080x720")
        # minimum dimension of the window
        self.minsize(800,720)
        # bachground color
        self.config(background='grey')
        # label text
        label = tk.Label(self, text="Projet transverse : efrei Paris", font=('Times','80'),bg='grey')
        label.pack(side="top", anchor="nw", padx=10, pady=20)       

        # Menu configuration
        self.title("Interface SAVEP")

        menubar = Menu(self)
        self.config(menu=menubar)
        # Menu Rechercher
        fileMenu = Menu(menubar, tearoff=0)
        submenu = Menu(fileMenu, tearoff=0)
        submenu.add_command(label='Recherche des vidéos par mot clé sur Youtube',command=lambda: self.show_frame(PageSeven))
        fileMenu.add_cascade(label='Importer', menu=submenu, underline=0)

        fileMenu.add_command(label="Quitter", command=self.on_exit)
        menubar.add_cascade(label="Rechercher", menu=fileMenu)

        # Container configuration
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageSeven):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def on_exit(self):
        """Close all"""
        if messagebox.askokcancel( self.title(), "Attention, Voulez-vous vraiment quitter ce programme ?", parent=self):
            self.destroy()    
       
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Projet transverse", font=('Times','50'))
        label.pack(pady=10,padx=10)
       
        # global picture of the project
        self.photo = Image.open("images/logoefrei.png")
        self.photo = self.photo.resize((800, 296), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.photo)
        self.canvas = Canvas(self, width=800, height=296, bg='grey99')
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        self.canvas.pack(side=TOP, padx=0, pady=0, anchor=CENTER)
       
        button4 = tk.Button(self, text="Button4",
                            command=lambda: controller.show_frame(PageFour))
        button4.pack(side=RIGHT, padx=10, pady=10, anchor=SE)

        button3 = tk.Button(self, text="Button3",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack(side=RIGHT, padx=10, pady=10, anchor=SE)

        Button3 = tk.Button(self, text="Button2",
                            command=lambda: controller.show_frame(PageTwo))
        Button3.pack(side=RIGHT, padx=10, pady=10, anchor=SE)

        button = tk.Button(self, text="Button1",
                            command=lambda: controller.show_frame(PageOne))
        button.pack(side=RIGHT,padx=10, pady=10, anchor=SE)

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
       
        label = tk.Label(self, text="Button1", font="Times 40 italic bold")
        label.pack(pady=10,padx=10)

        text_id = "It's up to you to play the game ^_^ \n Write here your text or adapt it according to your needs or delete it :) \n Don't forget teamwork :p"
        context = tk.Message(self, width=1200, pady=20, text = text_id,justify=LEFT,anchor=E,relief = SUNKEN)
        context.config(bg='grey99', font=('times', 20, 'italic'))
        context.pack(pady=0, expand=True)
       
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(side=RIGHT, padx=10, pady=10, anchor=SE)

        button4 = tk.Button(self, text="Button4",
                            command=lambda: controller.show_frame(PageFour))
        button4.pack(side=RIGHT, padx=10, pady=10, anchor=SE)

        button3 = tk.Button(self, text="Button3",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack(side=RIGHT, padx=10, pady=10, anchor=SE)

        Button3 = tk.Button(self, text="Button2",
                            command=lambda: controller.show_frame(PageTwo))
        Button3.pack(side=RIGHT, padx=10, pady=10, anchor=SE)

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Button2", font="Times 40 italic bold")
        label.pack(pady=10,padx=10)

        text_id = "It's up to you to play the game ^_^ \n Write here your text or adapt it according to your needs or delete it :) \n Don't forget teamwork :p"
        context = tk.Message(self, width=1200, pady=20, text = text_id,justify=LEFT,anchor=E,relief = SUNKEN)
        context.config(bg='grey99', font=('times', 20, 'italic'))
        context.pack(pady=0, expand=True)
       
        self.domain = Image.open("images/equipe.jpg")
        self.domain = self.domain.resize((500, 500), Image.ANTIALIAS)
        self.domain = ImageTk.PhotoImage(self.domain)
        self.canvas = Canvas(self, width=500, height=500, bg='grey99')
        self.canvas.create_image(0, 0, anchor=NW, image=self.domain)
        self.canvas.pack(side=TOP, padx=0, pady=0, anchor=CENTER)
       
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(side=RIGHT, padx=10, pady=10, anchor=SE)

        button4 = tk.Button(self, text="Button4",
                            command=lambda: controller.show_frame(PageFour))
        button4.pack(side=RIGHT, padx=10, pady=10, anchor=SE)

        button3 = tk.Button(self, text="Button3",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack(side=RIGHT, padx=10, pady=10, anchor=SE)

        Button3 = tk.Button(self, text="Button1",
                            command=lambda: controller.show_frame(PageOne))
        Button3.pack(side=RIGHT, padx=10, pady=10, anchor=SE)

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Button3", font="Times 40 italic bold")
        label.pack(pady=10,padx=10)
       
        text_id = "It's up to you to play the game ^_^ \n Write here your text or adapt it according to your needs or delete it :) \n Don't forget teamwork :p"
        context = tk.Message(self, width=1200, pady=20, text = text_id,justify=LEFT,anchor=E,relief = SUNKEN)
        context.config(bg='grey99', font=('times', 20, 'italic'))
        context.pack(pady=0, expand=True)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(side=RIGHT, padx=10, pady=10, anchor=SE)

        button4 = tk.Button(self, text="Button4",
                            command=lambda: controller.show_frame(PageFour))
        button4.pack(side=RIGHT, padx=10, pady=10, anchor=SE)

        button3 = tk.Button(self, text="Button2",
                            command=lambda: controller.show_frame(PageTwo))
        button3.pack(side=RIGHT, padx=10, pady=10, anchor=SE)

        Button3 = tk.Button(self, text="Button1",
                            command=lambda: controller.show_frame(PageOne))
        Button3.pack(side=RIGHT, padx=10, pady=10, anchor=SE)

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Button4", font="Times 40 italic bold")
        label.pack(pady=10,padx=10)
       
        text_id = "It's up to you to play the game ^_^ \n Write here your text or adapt it according to your needs or delete it :) \n Don't forget teamwork :p"
        context = tk.Message(self, width=1200, pady=20, text = text_id,justify=LEFT,anchor=E,relief = SUNKEN)
        context.config(bg='grey99', font=('times', 30, 'italic'))
        context.pack(pady=0, expand=True)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(side=RIGHT, padx=10, pady=10, anchor=SE)

        button4 = tk.Button(self, text="Button3",
                            command=lambda: controller.show_frame(PageThree))
        button4.pack(side=RIGHT, padx=10, pady=10, anchor=SE)

        button3 = tk.Button(self, text="Button2",
                            command=lambda: controller.show_frame(PageTwo))
        button3.pack(side=RIGHT, padx=10, pady=10, anchor=SE)

        Button3 = tk.Button(self, text="Button1",
                            command=lambda: controller.show_frame(PageOne))
        Button3.pack(side=RIGHT, padx=10, pady=10, anchor=SE)

class PageSeven(tk.Frame):
    def __init__(self, parent, controller):
        self.pause = False   # Parameter that controls pause button
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Recherche de vidéos par mot clé sur Youtube", font="Times 40 italic bold")
        label.grid(column=1,sticky=NW)
        
        self.delay = 15   # ms
        self.canvas = Canvas(self, width=1000, height=620)
        self.canvas.grid(column=1, row=0, padx=200, pady=100)
    
        def openNewWindow(self):
            def Youtube(self):
                videosSearch = VideosSearch(motcle, limit = 50)
                for keys, values in videosSearch.result().items():
                    res = values[0:11]
                    link_list = []
                    i=0
                    while i<10:
                        res1 = res[i]
                        for key, value in res1.items():
                            if key == 'link':
                                link_list.append(value)
                                i+=1

                    label = tk.Label(self, text="Les dix premiers résultats de la recherche avec le mot clé ''"+motcle+"'' sont :\n\n", justify=LEFT, anchor=NE)
                    label.grid(column=3, sticky="NE", padx=800)
                    label.place(x=300, relx=0.8, rely=0.15, anchor=NE)

                    passortie = 0.2
                    j=1
                    for i in link_list:
                        print(i+"\n")
                        label1 = tk.Label(self, text="Sortie "+str(j)+" : "+i+"\n", justify=LEFT, anchor=NE)
                        label1.grid(column=3, sticky="NE", padx=800)
                        label1.place(x=300, relx=0.8, rely=passortie, anchor=NE)
                        passortie += 0.05
                        # Get first result
                        if j == 1:
                            global url_firstvideo
                            url_firstvideo = i
                        j+=1
            
            def show_entry_fields(self):
                global motcle
                motcle = keyword.get()
                if len(keyword.get()) == 0:
                    label2 = tk.Label(self, text="Aucun mot clé saisi ! Merci de saisir votre mot clé.\n", justify=LEFT, anchor=NE)
                    label2.grid(column=3, sticky="NE", padx=800)
                    label2.place(x=300, relx=0.8, rely=0.05, anchor=NE)
                else:
                    label3 = tk.Label(self, text="Le mot clé saisi pour recherche sur Youtube est :\t''"+motcle+"''\n", justify=LEFT, anchor=NE)
                    label3.grid(column=3, sticky="NE", padx=800)
                    label3.place(x=300, relx=0.8, rely=0.1, anchor=NE)

            # Toplevel object which will be treated as a new window
            newWindow = Toplevel(self)
            # sets the title of the Toplevel widget
            newWindow.title("Mot clé de recherche")
            # sets the geometry of toplevel
            newWindow.geometry("750x100")
            # A Label widget to show in toplevel
            Label(newWindow,text ="Saisissez votre mot clé de recherche").grid(row=0,column=2, pady=10)
            # widget to enter keyword
            tk.Label(newWindow, text="Mot clé").grid(row=3, column=0, padx=10)

            keyword = tk.Entry(newWindow)
            keyword.grid(row=3, column=1, padx=0, pady=15, sticky="nsew")
            # Research button
            Button3 = tk.Button(newWindow, text="Obtenir le mot-clé saisi",command=lambda:show_entry_fields(self))
            Button3.grid(row=3, column=2, padx=0, pady=15, sticky="nsew")

            button = tk.Button(newWindow, text="Lancer la recherche",command=lambda:Youtube(self))
            button.grid(row=3, column=3, padx=0, pady=15, sticky="nsew")

            button1 = tk.Button(newWindow, text="Quitter",command=lambda:newWindow.destroy())
            button1.grid(row=3, column=4, padx=0, pady=15, sticky="nsew")

        def LoadFirstRes(self, url):
            global pathfile
            self.delay = 15 # delay in ms to get the latest frame
            youtube = pytube.YouTube(url)
            video = youtube.streams.first()
            filePath = "./FirstYouResVideo"
            video.download(filePath)
            # Get file name
            filename = os.listdir(filePath)
            pathfile = filePath+'/'+filename[0]
            print(pathfile)
            
            self.cap = cv2.VideoCapture(pathfile)
            self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            
            # Create canvas for image
            self.canvas = Canvas(self, width=1000, height=620)
            self.canvas.config(width = 1000, height = 620)
            
            # Create canvas for image
            self.canvas = Canvas(self, width=1000, height=620)
            self.canvas.grid(column=1, row=0, padx=200, pady=100)
            # image
            self.image = cv2.cvtColor(self.cap.read()[1], cv2.COLOR_BGR2RGB) # to RGB
            self.image = cv2.resize(self.image, (1000, 620))
            self.image = Image.fromarray(self.image) # to PIL format
            self.image = ImageTk.PhotoImage(self.image) # to ImageTk format
            # Update image
            self.canvas.create_image(0, 0, anchor=tk.NW, image = self.image)
            
            label = tk.Label(self, text="La vidéo a été chargée avec succès\n", justify=LEFT, anchor=NE)
            label.grid(column=3, sticky="NE", padx=800)
            label.place(x=300, relx=0.8, rely=0.7, anchor=NE)

        def get_frame(self):
            try:
                if self.cap.isOpened():
                    ret, frame = self.cap.read()
                    return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            except:
                messagebox.showerror(title='Video file not found', message='Please select a video file.')

        def play_video(self):
            ret, frame = get_frame(self)
            if ret:
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
                self.canvas.create_image(0, 0, image = self.photo, anchor = NW)
            if not self.pause:
                self.window.after(self.delay, play_video(self))

        def pause_video(self):
            self.pause = True

        #Addition
        def resume_video(self):
            self.pause=False
            play_video(self)

        # Release the video source when the object is destroyed
        def __del__(self):
            if self.cap.isOpened():
                self.cap.release()

        Button3 = tk.Button(self, text="Rechercher une vidéo", width = 15, command=lambda:openNewWindow(self))
        Button3.grid(column=0, padx=5)
        Button3.place(relx=0.01, rely=0.1, anchor=NW)

        button3 = tk.Button(self, text="Charger la vidéo", width = 15, command=lambda:LoadFirstRes(self, url_firstvideo))
        button3.grid(column=0, padx=5)
        button3.place(relx=0.01, rely=0.15, anchor=NW)

        button4 = tk.Button(self, text="Play", width = 15, command=lambda:play_video(self))
        button4.grid(column=0, padx=5)
        button4.place(relx=0.01, rely=0.2, anchor=NW)

        button5 = tk.Button(self, text="Pause", width = 15, command=lambda:pause_video(self))
        button5.grid(column=0, padx=5)
        button5.place(relx=0.01, rely=0.25, anchor=NW)

        button6 = tk.Button(self, text="Resume", width = 15, command=lambda:resume_video(self))
        button6.grid(column=0, padx=5)
        button6.place(relx=0.01, rely=0.3, anchor=NW)

        button1 = tk.Button(self, text="Back to Home", width = 15, command=lambda: controller.show_frame(StartPage))
        button1.grid(column=0, padx=5)
        button1.place(relx=0.01, rely=0.35, anchor=NW)        

app = SeaofBTCapp()
app.mainloop()
