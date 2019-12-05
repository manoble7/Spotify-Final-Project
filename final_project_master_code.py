#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: madelinenoble
"""

import spotipy
import spotipy.oauth2 as oauth2
import playlist_dictionary
import user_interface
import random
import spotipy.util as util
from datetime import date


def reformat_input_string(input_str):
    '''
    This function will reformat the user input so that it matches the style of the keys in the playlist dictionary. This means, capitalized letters for each word and no spaces in between the words.

    **Parameters**
        inpiut: *str*
            the input string given by the user

    **Returns**
        formatted_input: *str*
            the user input reformatted to fit the style of the playlist
            dictionary
    '''

    formatted_input = input_str.capitalize().strip()

    return formatted_input


def convert_time_to_mseconds(hours, minutes):
    '''
    This function converts the number of hours and number of minutes into
    total number of milliseconds

    **Parameters**
        hours: *int*
            the number of hours the new playlist should be

        minutes: *int*
            the number of minutes the new playlist should be

    **Returns**
        *int*
        total milliseconds
    '''
    return int(hours) * 3600000 + int(minutes) * 60000


def BPM(min_BPM, max_BPM, music_type, username, hours, minutes, playlist_name):
    '''
    This function call another function to determine the songs that are in
    the specified BPM then it generates the playlist

    **Parameters**
        music_type: *str*
            the genre of music the user wants the playlist to be.
            If none is specified, the default playlist to access is US top 100.

        min_BPM: *int*
            lower bound for BPM range, as specified by user

        max_BPM: *int*
            upper bound for BPM range, as specified by user

    **Returns**

        none
    '''
    # get the credentials of teh app
    # the app is based on the spotify developer website and this is where the
    # cliend id and secret come from
    credentials = oauth2.SpotifyClientCredentials(client_id="ec9bf5bbdcda4e3ebb4e5b3fe719f1ea", client_secret="2a0aede0c27246b19dff50617b4723b4")
    # get a token to access the app
    token = credentials.get_access_token()
    # authorize the token
    spotify = spotipy.Spotify(auth=token)

    time = convert_time_to_mseconds(hours, minutes)

    playlist_time = 0  # length of the playlist that we are generating
    playlist = list()  # list for the Ids of the playlist
    counter = 0  # counter that keeps track of the playlist in the genere
    used_id_list = list()


    good_songs, good_song_times = get_songs_in_BPM_range(spotify, music_type, counter, min_BPM, max_BPM)
    # loop through the playlists for a genere until either the target time is
    # reached or the playlists are all used up
    while playlist_time < time:

        if len(good_songs) == 0:
            counter = counter + 1
            if counter >= 6:
                if playlist_time == 0:
                    user_interface.pop_up_fun('no songs in that range')
                    quit
                else:
                    playlist_gen(playlist, time, username, music_type, min_BPM, max_BPM)
                    user_interface.pop_up_fun('Your playlist has been created but there were not enough songs in that BPM range to meet your time limit')
                    quit
            # generate new list of good songs and times from another playlist
            # from the specified genere
            good_songs, good_song_times = get_songs_in_BPM_range(spotify, music_type, counter, min_BPM, max_BPM)

        else:
            choice = random.choice(good_songs)
            index = good_songs.index(choice)

            # check if the track has already been added to the new playlist
            if choice in playlist:
                pass
            else:
                index = good_songs.index(choice)
                playlist.append(choice)
                playlist_time = playlist_time + good_song_times[index]
                used_id_list.append(choice)

            good_songs.remove(choice)
            good_song_times.remove(good_song_times[index])
 
    playlist_gen(playlist, time, username, music_type, min_BPM, max_BPM, playlist_name)



def get_songs_in_BPM_range(spotify, music_type, playlist_counter, min_BPM, max_BPM):
    '''
    This function gets tracks from a playlist that are in the correct BPM range

    **Parameters**
        music_type: list, genere of music
        playlist_counter: intz; keeps track of what playlist we are looking at
        in a specific genere
        min_BPM: user specified minimum BPM
        max_BPM: user specified maximum BPM

    **Returns**

        good_songs: list: list of all the ids of the songs within the specified
        BPM
        good_song_times: lsit: list of all the durations of the songs within
        the specified BPM
    '''
    # get the id of the playlist whose songs we are looking at
    # print(playlist_counter)
    type_uri = playlist_dictionary.get_playlist_ID(music_type, playlist_counter)
    # get the songs in the playlist
    tracks = spotify.user_playlist_tracks('Spotify', playlist_id=type_uri, fields=None, limit=100, offset=0, market=None)



    good_songs = list()  # list for songs that are in the specified range
    good_song_times = list()  # list of the durations of the good songs
    id_list = list()  # ids of songs used so that we do not repeat songs
    features = list()  # list of the features of each song in the spotify playlist

    # the audio_features function in spotipy only takes in 50 items at a time
    # the number of tracks in the playlist we are pulling from must be split
    # into groups of 50 and the remainder
    loops_50 = len(tracks['items'])//50
    loops_remainder = len(tracks['items']) % 50
    counter = 0  # keeps track of what track we are on in the playlist

    # get the features for the tracks, this includes the tempo (average BPM)
    # of each song which we use later

    for i in range(loops_50):
        id_list = list()
        for k in range(50):
            try:
                id_list.append(tracks['items'][counter]['track']['id'])
                counter = counter + 1
            except TypeError:
                counter = counter + 1
                pass
        features.extend(spotify.audio_features(id_list))
    
    id_list = list()
    for i in range(loops_remainder):
        try:
            id_list.append(tracks['items'][counter]['track']['id'])
            counter = counter + 1
        except TypeError:
            counter = counter + 1
    features.extend(spotify.audio_features(id_list))

    # if user specifies a single BPM then find songs with a range of +- 5 BPMs
    if min_BPM == max_BPM:
        BPM = min_BPM
        for i in range(len(features)):
            # get the tracks with the bpm in range
            if features[i]['tempo'] >= BPM - 5 and features[i]['tempo'] <= BPM + 5:
                good_songs.append(features[i]['id'])
                good_song_times.append(features[i]['duration_ms'])
    else:

        for i in range(len(features)):
            try:
                # print(features[i]['tempo'])
                if features[i]['tempo'] >= min_BPM and features[i]['tempo'] <= max_BPM:
                    good_songs.append(features[i]['id'])
                    good_song_times.append(features[i]['duration_ms'])
            except TypeError:
                pass

    return good_songs, good_song_times


def playlist_gen(playlist, time, username, music_type, min_BPM, max_BPM, playlist_name):

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
    # generate token for authorizations
    token = get_token(username)
    # get authorization to create a playlist
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    # get playlist name
    if playlist_name == '':
        playlist_name = get_playlist_name(time, music_type, min_BPM, max_BPM)
    # create the playlist
    new_playlist = sp.user_playlist_create(username, playlist_name, public=True)
    # get new playlists id
    playlist_id = new_playlist['id']
    # add tracks to the playlist but first check if the number of songs is
    # greater than 50 since we can only add 50 songs at a time
    if len(playlist) > 100:
        playlist_counter = 0
        playlist_100_loops = len(playlist)//100
        playlist_100_rem = len(playlist)%100
        playlist_counter = 0

        for i in range(playlist_100_loops):
            playlist_add = list()
            for k in range(100):
                playlist_add.append(playlist[playlist_counter])
                playlist_counter = playlist_counter + 1
            sp.user_playlist_add_tracks(username, playlist_id, playlist_add, position=None)

        playlist_add = list()
        for i in range(playlist_100_rem):
            playlist_add.append(playlist[playlist_counter])
            playlist_counter = playlist_counter + 1
        sp.user_playlist_add_tracks(username, playlist_id, playlist_add, position=None)
    else:
        sp.user_playlist_add_tracks(username, playlist_id, playlist, position=None)


def get_playlist_name(time, music_type, BPM_min, BPM_max):
    '''
    This function takes in all of the information about the playlist and
    creates a name for the playlist

    **Parameters**
        time: length of the playlist
        music_type: string, genere of the playlist
        BPM_min: int, user specified minimum BPM for the playlist
        BPM_max: int, user specified maximum BPM for the playlist

    **Returns**

        string: name of the playlist
    '''

    BPM = str((BPM_min + BPM_max)/2)
    # convert the time from milliseconds into hours and minutes
    hours = time // 3600000
    minutes = (time % 3600000)/60000
    # get todays date for the playlist
    current_date = str(date.today().strftime("%b_%d_%Y"))

    return current_date + '_' + music_type + '_Hours:' + str(hours) + '_Minutes:' + str(minutes) + '_BPM:' + BPM


def get_token(username):
    '''
    This function takes in the username and authorizes a token so that this
    app can create a playlist in the users profile

    **Parameters**
        username: string: username of the user

    **Returns**

        token if authorized and exits the script if not authorized
    '''
    # spotify will prompt the user to input their credentials so that
    # spotify can verify the users interaction with the app
    token = util.prompt_for_user_token(username, scope='playlist-modify-public', client_id='ec9bf5bbdcda4e3ebb4e5b3fe719f1ea', client_secret="2a0aede0c27246b19dff50617b4723b4", redirect_uri= 'https://mysite.com/redirect')

    if token:
        return token
    else:
        print("Can't get token for", username)
        exit()
