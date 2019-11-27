#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: madelinenoble
"""

import spotipy
import spotipy.oauth2 as oauth2
import playlist_dictionary
import random


def BPM():
    '''
    This function determines all of the songs in a certain playlist that are
    within the range for the BPM.

    **Parameters**
        none

    **Returns**

        none
    '''

    credentials = oauth2.SpotifyClientCredentials(client_id="ec9bf5bbdcda4e3ebb4e5b3fe719f1ea",client_secret="2a0aede0c27246b19dff50617b4723b4")
    token = credentials.get_access_token()
    spotify = spotipy.Spotify(auth=token)

    Mtype = 'EDM'
    # Mtype = input("What type of music do you want? ")
    # BPM = input("What pace do you want? ")

    type_uri = playlist_dictionary.get_playlist_ID(Mtype)
    tracks = spotify.user_playlist_tracks('Spotify', playlist_id=type_uri, fields=None, limit=100, offset=0, market=None)

    good_songs = list()
    id_list = list()
    loops_50 = len(tracks['items'])//50
    loops_remainder = len(tracks['items']) % 50
    counter = 0
    features = list()
    BPM = 125
    good_song_times = list()

    for i in range(loops_50):
        for k in range(50):
            id_list.append(tracks['items'][counter]['track']['id'])
            counter = counter + 1
        features.extend(spotify.audio_features(id_list))

    for i in range(loops_remainder):
        id_list.append(tracks['items'][counter]['track']['id'])
        counter = counter + 1
    features.extend(spotify.audio_features(id_list))

    for i in range(len(features)):
        if features[i]['tempo'] >= BPM - 1 and features[i]['tempo'] <= BPM + 1:
            good_songs.append(features[i]['id'])
            good_song_times.append(features[i]['duration_ms'])

    playlist_gen(good_songs, good_song_times, 3600000)


def playlist_gen(good_songs, good_song_times, time = 3600000):
      '''
    This function takes all of the songs that have the correct BPM and creates
    a playlist of the specified length

    **Parameters**
        good_songs: list, list of all of the songs that have the correct BPM
        good_songs_times: list, list of all of the good songs durations
        time: user specified length of the playlist

    **Returns**

        none
    '''
    credentials = oauth2.SpotifyClientCredentials(client_id="ec9bf5bbdcda4e3ebb4e5b3fe719f1ea", client_secret="2a0aede0c27246b19dff50617b4723b4")
    token = credentials.get_access_token()
    spotify = spotipy.Spotify(auth=token)
    playlist_time = 0
    playlist = list()

    while playlist_time < time:
        choice = random.choice(good_songs)
        index = good_songs.index(choice)
        playlist.append(choice)
        good_songs.remove(choice)
        playlist_time = playlist_time + good_song_times[index]
        good_song_times.remove(good_song_times[index])

    spotify.user_playlist_create(user = 'manoble3' , name = "new", public=True)      
    

    
if __name__ == "__main__":
    BPM()
