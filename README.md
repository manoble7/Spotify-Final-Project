# Spotify-Final-Project
Spotify final project

To Do:

- Drop down menu for bpm input
- Exception if user is not found (users for Spotify)
- Add more playlists to the dictionary
- Add more filters: 
    - Mood
    - Energy 
- Maybe Apple Watch thing where it takes your bpm and gives you the next song (queues a song that matches your bpms or the bpm you want to target)
- Write the ReadMe file
- Handle:
    - Not enough songs for the time specified by user
    - If username doesn’t exist
- Look into if token has expired how to regenerate without having to copy the link all the time
- Add a random option for song genre that picks songs from all playlists as long as a target bpm/range is given
    - Handle exception where no bpm is given
- Toggle buttons for if user wants a range of bpm or a specified bpm
- Check to see what features audio_features() gets for each track


Our Final Project for Software Carpentry class consists of a program that allows the user to generate a playlist based on a target BPM or BPM range. The program allows a user to specify the type of music they want to include in the playlist, the total duration of the playlist, and the BPM target or range that will match the type of activity to be done. The playlists generated can be used for anything from running, walking, yoga, meditation, or even sleep (set it to 8 hours of calm music). 

We used Spotify's API to search through existing playlists for the songs that match the user's specifications (bpm, mood, energy, genre) and extend a list of songs until the target time length of the activity is met. In order to access Spotify's API we created a developer ID which generated a set of credentials. These credentials authorize us to access Spotify's data in a secure manner, and allow us to create a playlist within a user's account (the user must first log in through the app). 

The file "playlist_dictionary.py" contains a dictionary of playlists, where the keys are the different music genres and the values are each playlist's corresponding Spotify ID (which is needed to access that particular playlist through the API). The file also contains two methods: get_playlist_ID(key) takes in the music genre (or key) and returns the ID of said playlist, and get_keys() returns all the keys in the dictionary. Both methods are used in the main script.

The file "final_project_master_code.py" is the main script. 


The file "user_interface.py" handles the interaction with the user. This is where the user inputs all the desired specifications to generate the playlist. The script uses python's tkinter method, which is one of the most common graphical user interfaces (GUI). 
