#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 08:28:22 2019

@author: madelinenoble
"""
import spotipy
import spotipy.oauth2 as oauth2
import unittest
import final_project_master_code
import playlist_dictionary


class TestStringMethods(unittest.TestCase):

    def test_convert_time_to_msseconds(self):
        '''
        Function ensures that the time is coverted properly
        '''
        hours = 9
        minutes = 30
        ms = 34200000

        self.assertEqual(final_project_master_code.convert_time_to_mseconds(hours, minutes), ms)

    def test_get_songs_in_BPM_with_range(self):
        '''
        Function ensures the correct songs are returned in the BPM range
        '''
        credentials = oauth2.SpotifyClientCredentials(client_id="ec9bf5bbdcda4e3ebb4e5b3fe719f1ea", client_secret="2a0aede0c27246b19dff50617b4723b4")
        token = credentials.get_access_token()
        spotify = spotipy.Spotify(auth=token)
        music_type = 'Pop: average BPM range = 100 - 140'
        playlist_counter = 0
        self.assertEqual(final_project_master_code.get_songs_in_BPM_range(spotify, music_type, playlist_counter, 160, 170), (['57vxBYXtHMk6H1aD29V7PU', '00Z0GIRi0l7WqQnQJCo5S2'], [200080, 196160]))

    def test_get_songs_in_BPM_with_singe_num(self):
        '''
        Function ensures the correct songs are returned in the BPM range when
        one BPM
        '''
        credentials = oauth2.SpotifyClientCredentials(client_id="ec9bf5bbdcda4e3ebb4e5b3fe719f1ea", client_secret="2a0aede0c27246b19dff50617b4723b4")
        token = credentials.get_access_token()
        spotify = spotipy.Spotify(auth=token)
        music_type = 'ClassicRock: average BPM range= 90 - 130'
        playlist_counter = 1

        self.assertEqual(final_project_master_code.get_songs_in_BPM_range(spotify, music_type, playlist_counter, 175, 175), (['12XBk6u0E6HIkrjImA3tzC'], [271491]))

    def test_get_playlist_ID(self):
        '''
        Function ensures the proper ID is returned
        '''
        key = 'HipHop: average BPM ranage = 80 - 115'
        counter = 3
        self.assertEqual(playlist_dictionary.get_playlist_ID(key, counter), 'spotify:playlist:37i9dQZF1DX6GwdWRQMQpq')


if __name__ == '__main__':

    unittest.main()
