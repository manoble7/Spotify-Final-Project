#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: madelinenoble
"""

import spotipy
import spotipy.oauth2 as oauth2
import playlist_dictionary
import random
import spotipy.util as util
from datetime import datetime
from datetime import date


def reformat_input_string(input_str):
    '''
    This function will reformat the user input so that it matches the style of the keys in the playlist dictionary. This means, capitalized letters for each word and no spaces in between the words.

    **Parameters**
        inpiut: *str*
            the input string given by the user

    **Returns**
        formatted_input: *str*
            the user input reformatted to fit the style of the playlist dictionary
    '''

    formatted_input = input_str.capitalize().strip()

    return formatted_input

def convert_time_to_msseconds(hours, minutes):
    return int(hours)*3600000 +int(minutes)*60000

def BPM(min_BPM, max_BPM, music_type, username, hours, minutes):
    '''
    This function determines all of the songs in a certain playlist that are
    within the range for the BPM.

    **Parameters**
        music_type: *str*
            the genre of music the user wants the playlist to be. If none is specified, the default playlist to access is US top 100. 

        min_BPM: *int* 
            lower bound for BPM range, as specified by user

        max_BPM: *int*
            upper bound for BPM range, as specified by user

    **Returns**

        none
    '''

    credentials = oauth2.SpotifyClientCredentials(client_id="ec9bf5bbdcda4e3ebb4e5b3fe719f1ea",client_secret="2a0aede0c27246b19dff50617b4723b4")
    token = credentials.get_access_token()
    spotify = spotipy.Spotify(auth=token)

    type_uri = playlist_dictionary.get_playlist_ID(music_type, counter=0)
    tracks = spotify.user_playlist_tracks('Spotify', playlist_id=type_uri, fields=None, limit=100, offset=0, market=None)

    good_songs = list()
    id_list = list()
    features = list()
    good_song_times = list()
    loops_50 = len(tracks['items'])//50
    loops_remainder = len(tracks['items']) % 50
    counter = 0

    for i in range(loops_50):
        for k in range(50):
            id_list.append(tracks['items'][counter]['track']['id'])
            counter = counter + 1
        features.extend(spotify.audio_features(id_list))

    for i in range(loops_remainder):
        id_list.append(tracks['items'][counter]['track']['id'])
        counter = counter + 1
    features.extend(spotify.audio_features(id_list))

    # if user specifies a single BPM then find songs with a range of +- 5 BPMs
    if min_BPM == max_BPM:
        BPM = min_BPM
        for i in range(len(features)):
            if features[i]['tempo'] >= BPM - 5 and features[i]['tempo'] <= BPM + 5:
                good_songs.append(features[i]['id'])
                good_song_times.append(features[i]['duration_ms'])

    else:
        for i in range(len(features)):
            if features[i]['tempo'] >= min_BPM and features[i]['tempo'] <= max_BPM:
                good_songs.append(features[i]['id'])
                good_song_times.append(features[i]['duration_ms'])

    time = convert_time_to_msseconds(hours, minutes)
    playlist_gen(good_songs, good_song_times, time, username, music_type, min_BPM, max_BPM)


def playlist_gen(good_songs, good_song_times, time, username, music_type, min_BPM, max_BPM):

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

    playlist_time = 0
    playlist = list()

    while playlist_time < time:
        choice = random.choice(good_songs)
        index = good_songs.index(choice)
        playlist.append(choice)
        good_songs.remove(choice)
        playlist_time = playlist_time + good_song_times[index]
        good_song_times.remove(good_song_times[index])

    token = get_token(username)
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    playlist_name = get_playlist_name(time, music_type, min_BPM, max_BPM)
    new_playlist = sp.user_playlist_create('manoble3', playlist_name, public=True)
    playlist_id = new_playlist['id']
    sp.user_playlist_add_tracks(username, playlist_id, playlist, position=None)


def get_playlist_name(time, music_type, BPM_min, BPM_max):

    BPM = str((BPM_min + BPM_max)/2)
    hours = time // 3600000
    minutes = (time % 3600000)/60000
    current_date = str(date.today().strftime("%b_%d_%Y"))

    return current_date + '_' + music_type + '_Hours:' + str(hours) + '_Minutes:' + str(minutes) + '_BPM:' + BPM


def get_token(username):

    token = util.prompt_for_user_token(username, scope = 'playlist-modify-public', client_id='ec9bf5bbdcda4e3ebb4e5b3fe719f1ea', client_secret="2a0aede0c27246b19dff50617b4723b4", redirect_uri= 'https://mysite.com/redirect')

    if token:
        return token
    else:
        print("Can't get token for", username)
        exit()

#if __name__ == "__main__":
#
#    music_type_input = input("What type of music do you want? Type \"options\" to see available music types \n ")
#    if music_type_input == 'options':
#        print([key for key in playlist_dictionary.get_keys()])
#        music_type_input = input("What type of music do you want? ")
#
#    #music_type = reformat_input_string(music_type_input)
#    
##    print("What pace do you want? Input your target BPM or BPM range")
##    min_BPM = input("Mininmum beats per minute (BPM): ")
##    max_BPM = input("Maximum beats per minute (BPM): ")
#    music_type = "Pop"
#    min_BPM = 90
#    max_BPM = 140
#    print(type(min_BPM))
#    print(type(max_BPM))
#    BPM(min_BPM, max_BPM, music_type)
