# **Spotify Final Project**
## **Playlist generation using Spotify**
Project by Madelaine Noble and Lucia Sablich
Software Carpentry Fall 2019

**To Do:**

- [ ] Maybe Apple Watch thing where it takes your bpm and gives you the next song (queues a song that matches your bpms or the bpm you want to target)

### Overview:
Our Final Project for Software Carpentry class consists of a program that allows the user to generate a playlist based on a target BPM or BPM range. The program allows a user to specify the music genre they want to include in the playlist, the total duration of the playlist, and the BPM target or range that will match the type of activity to be done. The playlists generated can be used for anything from running, walking, yoga, meditation, or even sleep (try setting it to 8 hours of calm music). 

We used Spotify's API to search through existing playlists for the songs that match the user's specifications (bpm, mood, energy, genre) and extend a list of songs until the target time length of the activity is met. In order to access Spotify's API we created a developer ID which generated a set of credentials. These credentials authorize us to access Spotify's data in a secure manner, and allow us to create a playlist within a user's account (the user must first log in through the app). 

Upon inputting the Spotify username to be used, the program user is redirected to a Spotify website, where they must log in with their Spotify user and password in order to allow our program to create playlists within a user's account.

Sometimes the program user gets redirected to what seems like a crashed website. When this happens, the program user should copy the link of this website they've been redirected to and paste it into the terminal (there will be a prompt to paste the redirected link). After inputting the redirection link the program will continue to run. 

The user interface contains a BPM Help button that will pull up information on the relation between BPM and running/walking velocity, in units that are easier for the user to relate. 

### Running the code on Mac
To run the code open up Terminal and run the "user_interface.py" file using Python.
The program uses the tkinter module - a graphic user interface for python. However, new macOS versions (particularly macOS Mojave version 10.14.6) has some trouble running tkinter in python version 3.7.3. To address this bug we created a file called "requirements.txt" that includes a list of versions of the packages and modules for which the program doesn't crash. We recommend to create a new environment, install all the requirements and finally run the user_interface.py file in that environment. 

To do so, in Terminal run the following commands:

1. Make sure you exit any current environment by calling: conda deactivate
2. Then call: conda create --name myenv 
   (myenv is the name of your new environment, can be called anything you want)
3. Activate your new environment by calling: conda activate myenv
4. Install the requirements by calling: conda install --file requirements.txt
    
Now you should be ready to run the program without problems.

5. Run program with the call: python user_interface.py
   Make sure you are in the directory where the user_interface.py is located.
    

### Important Files:

##### Requirements
The "requirements.txt" file contains a list of all the modules and packages needed to run the code. These should be installed before trying to run the program. Instructions on how to install the requirements are found above. 

##### Playlist Dictionary
The file "playlist_dictionary.py" contains a dictionary of playlists, where the keys are the different music genres and the values are each playlist's corresponding Spotify ID (which is needed to access that particular playlist through the API). Each genre includes 6 playlists from which the songs are obtained. A "counter" variable is used to keep track of which playlist is being accessed (Think of it as an index).  The playlists dictionary is contained in a method: get_playlist_ID(key, counter). This method takes in the music genre (or key) and the counter number and returns the ID of the playlist specified by the genre and counter.

##### Master Code
The file "final_project_master_code.py" is the main script. 

##### User Interface 
The file "user_interface.py" handles the interaction with the user. This is where the user inputs all the desired specifications to generate the playlist. The script uses python's tkinter method, which is one of the most common graphical user interfaces (GUI). It prompts the user for a genre, the desired playlist length (time), a target BPM or BPM range, a name for the new playlist and the Spotify user account where the playlist will be created.
