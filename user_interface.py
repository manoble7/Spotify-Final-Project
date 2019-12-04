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
from tkinter import *
import final_project_master_code as mc


class App:

    def __init__(self, parent, generes, hours, minutes, BMP_nums): 
        self.contents = list()
        self.parent = parent
        self.parent.title('Spotify BMP Playlist')

        self.variable = StringVar(parent)
        self.variable.set(generes[0])  # default value
        self.label = Label(self.parent, text='Choose the type of genere you would like to listen to')
        self.label.grid(row=0, column=0, sticky=E)
        self.genere = OptionMenu(self.parent, self.variable, *generes)
        self.genere.grid(row=0, column=1, sticky=W)
        
        self.label = Label(self.parent, text='Put in the length you would like the playlist to be')
        self.label.grid(row=1, column=0, rowspan=2, sticky=E)
        self.variable1 = StringVar(parent)
        self.variable1.set(hours[0])
        self.label = Label(self.parent, text='Hours:')
        self.label.grid(row=3, column=0, sticky=E)
        self.hours = OptionMenu(self.parent, self.variable1, *hours)
        self.hours.grid(row=3, column=1, sticky=W)
        
        self.variable2 = StringVar(parent)
        self.variable2.set(minutes[0])
        self.label = Label(self.parent, text='Minutes:')
        self.label.grid(row=4, column=0, sticky=E)
        self.hours = OptionMenu(self.parent, self.variable2, *minutes)
        self.hours.grid(row=4, column=1, sticky=W)
        
        self.variable_min = StringVar(parent)
        self.variable_min.set(BPM_nums[0])
        self.label = Label(self.parent, text='Input the minimum value for the BPM range')
        self.label.grid(row=5, column=0, sticky=E)
        self.minimum = OptionMenu(self.parent, self.variable_min, *BPM_nums)
        self.minimum.grid(row=5, column=1, sticky=W)

        self.variable_max = StringVar(parent)
        self.variable_max.set(BPM_nums[75])
        self.maximum = Label(self.parent, text='Input the maximum value for the BPM range')
        self.maximum.grid(row=6, column=0, sticky=E)
        self.maximum = OptionMenu(self.parent, self.variable_max, *BPM_nums)
        self.maximum.grid(row=6, column=1, sticky=W)

        self.user = Label(self.parent, text='Input your username ')
        self.user.grid(row=7, column=0, sticky=E)
        self.user = Entry(self.parent, state=NORMAL)
        self.user.grid(row=7, column=1, sticky=W)

        self.R = Button(self.parent, text="BPM Help", command =lambda : BPM_info())
        self.R.grid(row=8, column=0, sticky=W)
        self.w = Button (self.parent, text='OK', command = lambda : self.use_entry())
        self.w.grid(row=8, column=1)


    def use_entry(self):
    
        self.contents = [self.variable_min.get(), self.variable_max.get(), self.variable.get(), self.user.get(), self.variable1.get(), self.variable2.get()]
        # do stuff with contents
        self.parent.destroy()

    def close(self):
            self.parent.destroy()

    def get_info(self):
        return self.contents


def pop_up_fun(message):
    master = Tk()
    end = pop_up_class(master, message)
    master.mainloop()


class pop_up_class:

    def __init__(self, parent, message):
        self.parent = parent
        self.window = Label(self.parent, text=message)
        self.window.pack()


def BPM_info():
    from PIL import Image, ImageTk

    root = tk.Tk()
    root.title('BPM Help')
    Label(root, text='The graph below can help you determine what \n your BPM is').pack()
    image = Image.open('BPM_info.png')
    render = ImageTk.PhotoImage(image, master=root)
    label = tk.Label(root, image=render)
    label.image = image
    label.pack()
    root.mainloop()


if __name__ == "__main__":
    master = Tk()
    generes = [
            ('ClassicRock: average BPM range= 90 - 130'),
            ("Pop: average BPM range = 100 - 140"),
            ("R&B: average BPM range = 80 - 110"),
            ("Rap"),
            ("Jazz: average BMP range = 60 - 120"),
            ("Country"),
            ("EDM: average BPM range = 120 - 180"),
            ("Calm: average BPM = 70 - 110"),
            ("IndieRock"),
            ("Instrumental: average BPM range = 85 - 125"),
            ('HipHop: average BPM ranage = 80 - 115')
        ]
    hours = [x for x in range(11)]
    minutes = [x for x in range(60)]
    BPM_nums = [x for x in range(50,180)]

    app = App(master, generes, hours, minutes, BPM_nums)
    master.mainloop()
    info = app.get_info()
    mc.BPM(int(info[0]), int(info[1]), info[2], info[3], info[4], info[5])
    pop_up_fun('Your playlist has been created!!')
    


