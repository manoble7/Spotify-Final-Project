#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: madelinenoble
"""

import spotipy
import spotipy.oauth2 as oauth2
import playlist_dictionary


def BPM():
    credentials = oauth2.SpotifyClientCredentials(client_id="ec9bf5bbdcda4e3ebb4e5b3fe719f1ea",client_secret="2a0aede0c27246b19dff50617b4723b4")
    token = credentials.get_access_token()
    spotify = spotipy.Spotify(auth=token)
    
    Mtype = 'EDM'
    #Mtype = input("What type of music do you want? ")
    #BPM = input("What pace do you want? ")
    
    type_uri = playlist_dictionary.get_playlist_ID(Mtype)
#    all_songs = spotify.get(type_uri)
    tracks = spotify.user_playlist_tracks('Spotify', playlist_id=type_uri, fields=None, limit=100, offset=0, market=None)
    print(type(tracks))
    audio = spotify.audio_analysis(tracks[1]['id'])

    


if __name__ == "__main__":
    BPM()
