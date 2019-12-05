#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 21:52:28 2019

@author: madelinenoble
"""

import tkinter as tk
from tkinter import *
import final_project_master_code as mc


class App:

    def __init__(self, parent, generes, hours, minutes, BMP_nums):
        '''
        This function initializes the window for the App

        **Parameters**
            parent: *object*
                the TK object which creates the window
            generes: *list*
                the list of generes that the user can pull from
            hours:*list*
                the list of hours that the user can pull from
            minutes: *list*
                a list of minutes, 1 - 59 for the user to choose
            BPM_nums: *list*
                list with the BPM numbers for the user to choose form

        **Returns**
            none
        '''

        self.contents = list()
        self.parent = parent
        self.parent.title('Spotify BMP Playlist')

        # create box and label for user to pick what genere they want
        self.variable = StringVar(parent)
        self.variable.set(generes[0])  # default value
        self.label = Label(self.parent, text='Choose the type of genere you would like to listen to')
        self.label.grid(row=0, column=0, sticky=E)
        self.genere = OptionMenu(self.parent, self.variable, *generes)
        self.genere.grid(row=0, column=1, sticky=W)

        # create box and label for user to pick what hours they want
        self.label = Label(self.parent, text='Put in the length you would like the playlist to be')
        self.label.grid(row=1, column=0, rowspan=2, sticky=E)
        self.variable1 = StringVar(parent)
        self.variable1.set(hours[0])
        self.label = Label(self.parent, text='Hours:')
        self.label.grid(row=3, column=0, sticky=E)
        self.hours = OptionMenu(self.parent, self.variable1, *hours)
        self.hours.grid(row=3, column=1, sticky=W)

        # create box and label for user to pick what minutes they want
        self.variable2 = StringVar(parent)
        self.variable2.set(minutes[0])
        self.label = Label(self.parent, text='Minutes:')
        self.label.grid(row=4, column=0, sticky=E)
        self.minutes = OptionMenu(self.parent, self.variable2, *minutes)
        self.minutes.grid(row=4, column=1, sticky=W)

        # create box and label for user to pick what BPM min they want
        self.variable_min = StringVar(parent)
        self.variable_min.set(BPM_nums[0])
        self.label = Label(self.parent, text='Input the minimum value for the BPM range')
        self.label.grid(row=5, column=0, sticky=E)
        self.minimum = OptionMenu(self.parent, self.variable_min, *BPM_nums)
        self.minimum.grid(row=5, column=1, sticky=W)

        # create box and label for user to pick what BPM max they want
        self.variable_max = StringVar(parent)
        self.variable_max.set(BPM_nums[75])
        self.maximum = Label(self.parent, text='Input the maximum value for the BPM range')
        self.maximum.grid(row=6, column=0, sticky=E)
        self.maximum = OptionMenu(self.parent, self.variable_max, *BPM_nums)
        self.maximum.grid(row=6, column=1, sticky=W)

        # create box and label for user to write the playlist name
        self.playlist_name = Label(self.parent, text='New playlist name: ')
        self.playlist_name.grid(row=7, column=0, sticky=E)
        self.playlist_name = Entry(self.parent, state=NORMAL)
        self.playlist_name.grid(row=7, column=1, sticky=W)

        # create box and label for user to write their username
        self.user = Label(self.parent, text='Input your Spotify username: ')
        self.user.grid(row=8, column=0, sticky=E)
        self.user = Entry(self.parent, state=NORMAL)
        self.user.grid(row=8, column=1, sticky=W)

        # create button that pops up a help window for BPM
        self.R = Button(self.parent, text="BPM Help", command=lambda: BPM_info())
        self.R.grid(row=9, column=0, sticky=W)

        # create an OK button that runs the program
        self.w = Button(self.parent, text='OK', command=lambda: self.use_entry())
        self.w.grid(row=9, column=1)

    def use_entry(self):
        '''
        This function takes in the user input and checks if it brings up
        any error

        **Parameters**
            none

        **Returns**
            none
        '''

        # check if the min is greater than the max
        if int(self.variable_min.get()) > int(self.variable_max.get()):
            pop_up_fun('Error: Min BPM cannot be larger than Max BPM',
                       "Error", False)

        # check that the user put in a username
        elif self.user.get() == '':
            pop_up_fun('Error: Please specify a Spotify username', "Error",
                       False)

        # check that the user specifies a length
        elif int(self.variable1.get()) == 0 and int(self.variable2.get()) == 0:
            pop_up_fun('Error: Please specify the playlist length', "Error",
                       False)

        else:
            self.contents = [self.variable_min.get(), self.variable_max.get(), self.variable.get(), self.user.get(), self.variable1.get(), self.variable2.get(), self.playlist_name.get()]
            self.parent.destroy()

    def get_info(self):
        '''
        This function returns the contects of the user input

        **Parameters**
            none

        **Returns**
            *list*
            contents of user input
        '''
        return self.contents


def pop_up_fun(message, title, button):
    '''
        This function creates a pop up window to give the user information

        **Parameters**
            message: *string*
                message to tell the user
            title: *string*
                title for the pop up box
            button: *boolean*
                whether or not there should be yes and no buttons in the
                window

        **Returns**
            none
    '''
    master = Tk()
    master.title(title)
    pop_up_class(master, message, button)
    master.mainloop()


class pop_up_class:

    def __init__(self, parent, message, button):
        '''
        This function initializes the pop up windon

        **Parameters**
            parent: *object*
                tkinter window object
            message: *string*
                message to tell the user
            button: *boolean*
                whether or not there should be yes and no buttons in the
                window
        **Returns**
            none
        '''

        self.parent = parent
        self.window = Label(self.parent, text=message)
        self.window.grid(row=0, column=0, columnspan=2)
        if button:
            self.w = Button(self.parent, text='Yes', command=lambda: self.button_set_true())
            self.w.grid(row=1, column=0, sticky=E)
            self.w = Button(self.parent, text='No', command=lambda: self.button_set_false())
            self.w.grid(row=1, column=1, sticky=W)

    def button_set_true(self):
        '''
        This function says that yes was pushed

        **Parameters**
           none
        **Returns**
            none
        '''
        self.button_tf = True
        self.parent.destroy()

    def button_set_false(self):
        '''
        This function says that no was pushed

        **Parameters**
           none
        **Returns**
            none
        '''
        self.button_tf = False
        self.parent.destroy()

    def get_button(self):
        '''
        This function returns the button answer

        **Parameters**
           none
        **Returns**
            *boolean*
            True if yes was pushed, false if no
        '''
        return self.button_tf


def BPM_info():
    '''
        This function creates a pop up window to give the user information
        about calculating BPM

        **Parameters**
            none

        **Returns**
            none
    '''
    # must inport PIL here becaue it isnt recognized when it is imported at
    # the top of the code
    from PIL import Image, ImageTk

    root = tk.Tk()
    root.title('BPM Help')
    # creating title and importing image for window
    Label(root, text='The graph below can help you determine what \n your BPM is').pack()
    image = Image.open('BPM_info.png')
    render = ImageTk.PhotoImage(image, master=root)
    label = tk.Label(root, image=render)
    label.image = image
    label.pack()
    root.mainloop()


if __name__ == "__main__":
    # generes that the user can pick from
    generes = [
            ('ClassicRock: average BPM range= 90 - 130'),
            ("Pop: average BPM range = 100 - 140"),
            ("R&B: average BPM range = 80 - 110"),
            ("Rap: average BPM range = 90 - 160"),
            ("Jazz: average BMP range = 60 - 120"),
            ("Country: average BPM range = 80 - 120"),
            ("EDM: average BPM range = 120 - 180"),
            ("Calm: average BPM = 70 - 110"),
            ("IndieRock: average BPM range = 100 - 130"),
            ("Instrumental: average BPM range = 85 - 125"),
            ('HipHop: average BPM ranage = 80 - 115'),
            ('Any genere')
        ]
    # creating lists for the user to pick from
    hours = [x for x in range(11)]
    minutes = [x for x in range(60)]
    BPM_nums = [x for x in range(50, 180)]

    # creaing the window
    master = Tk()
    app = App(master, generes, hours, minutes, BPM_nums)
    master.mainloop()
    info = app.get_info()

    mc.BPM(int(info[0]), int(info[1]), info[2], info[3], info[4], info[5],
           info[6])
    pop_up_fun('Your playlist has been created!!', 'Playlist Completed', False)
