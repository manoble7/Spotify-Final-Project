#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 21:52:28 2019

@author: madelinenoble
"""

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import *
import final_project_master_code as mc


class App:

    def __init__(self, parent, generes): 
        self.contents = list()
        self.parent = parent
        self.parent.title('Spotify BMP Playlist')
        self.variable = StringVar(parent)
        self.variable.set(generes[0])  # default value

        self.label = Label(self.parent, text='Choose the type of genere you would like to listen to')
        self.label.pack()

        self.genere = OptionMenu(self.parent, self.variable, *generes)
        self.genere.pack()

        self.label = Label(self.parent, text='Input the minimum value for the BPM range').pack()
        self.minimum = Entry(self.parent, state=NORMAL)
        self.minimum.pack()

        self.maximum = Label(self.parent, text='Input the maximum value for the BPM range')
        self.maximum.pack()
        self.maximum = Entry(self.parent, state=NORMAL)
        self.maximum.pack()

        self.user = Label(self.parent, text='Input your username ')
        self.user.pack()
        self.user = Entry(self.parent, state=NORMAL)
        self.user.pack()

        self.R = Button(self.parent, text="BPM Help", command =lambda : BPM_info())
        self.R.pack()
        self.w = Button (self.parent, text='OK', command = lambda : self.use_entry())
        self.w.pack()

        
    def use_entry(self):
    
        self.contents = [self.minimum.get(), self.maximum.get(), self.variable.get(), self.user.get()]
        # do stuff with contents
        self.close()

    def close(self):
            self.parent.destroy()

    def get_info(self):
        return self.contents


def BPM_info():
    from PIL import Image, ImageTk
    
    root = tk.Tk()
    root.title('BPM Help')
    Label(root, text='The graph below can help you determine what \n your BPM is').pack()
    image = Image.open('BPM_info.png')
    render = ImageTk.PhotoImage(image, master=root)
    label = tk.Label(root, image = render)
    label.image = image
    label.pack()
    root.mainloop()

if __name__ == "__main__":
    master = Tk()
    generes = [
            ('Classic Rock'),
            ("Pop"),
            ("R&B"),
            ("Rap"),
            ("Jazz"),
            ("Country"),
            ("EDM"),
            ("Calm"),
            ("Indie Rock"),
            ("Instrumental")
        ]

    app = App(master, generes)
    master.mainloop()
    info = app.get_info()
    mc.BPM(int(info[0]), int(info[1]), info[2], info[3])



