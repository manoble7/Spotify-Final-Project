
# Create dictionary with playlists to access given a particular genre parameter

# These are all playlists made by Spotify and updated fairly regularly (?)


def get_playlist_ID(key, counter):
    '''
    This function take in a type of music and returns a playlist id for that
    genere

    **Parameters**
        key: *string*
            the string for the dictionary for the type of genere

        counter: *int*
            the number of playlist that we want

    **Returns**
        *string*
        spotify id for playlist
    '''

    playlists = {
        'Country: average BPM range = 80 - 120': [
            'spotify:playlist:37i9dQZF1DX0XUsuxWHRQd',
            'spotify:playlist:37i9dQZF1DWYnwbYQ5HnZU',
            'spotify:playlist:37i9dQZF1DX8WMG8VPSOJC',
            'spotify:playlist:37i9dQZF1DXaiEFNvQPZrM',
            'spotify:playlist:37i9dQZF1DXdfhOsjRMISB',
            'spotify:playlist:37i9dQZF1DX1lVhptIYRda'],

        'ClassicRock: average BPM range= 90 - 130': [
            'spotify:playlist:37i9dQZF1DXdOEFt9ZX0dh',
            'spotify:playlist:37i9dQZF1DX0fWtUuB7bFE',
            'spotify:playlist:37i9dQZF1DWYNSm3Z3MxiM',
            'spotify:playlist:5BygwTQ3OrbiwVsQhXFHMz',
            'spotify:playlist:37i9dQZF1DWTwG3oGOElQX',
            'spotify:playlist:37i9dQZF1DWXRqgorJj26U'],

        'Pop: average BPM range = 100 - 140': [
            'spotify:playlist:37i9dQZF1DWUa8ZRTfalHk',
            'spotify:playlist:37i9dQZF1DXcZDD7cfEKhW',
            'spotify:playlist:37i9dQZF1DWXti3N4Wp5xy',
            'spotify:playlist:37i9dQZF1DX5gQonLbZD9s',
            'spotify:playlist:37i9dQZF1DX92MLsP3K1fI',
            'spotify:playlist:37i9dQZF1DXcBWIGoYBM5M'],

        'R&B: average BPM range = 80 - 110': [
            'spotify:playlist:37i9dQZF1DWYmmr74INQlb',
            'spotify:playlist:37i9dQZF1DX6VDO8a6cQME',
            'spotify:playlist:37i9dQZF1DX0H8hDpv38Ju',
            'spotify:playlist:37i9dQZF1DWUzFXarNiofw',
            'spotify:playlist:37i9dQZF1DX9zR5aXbFFRA',
            'spotify:playlist:37i9dQZF1DX4SBhb3fqCJd'],

        'Rap: average BPM range = 90 - 160': [
            'spotify:playlist:37i9dQZF1DXdnOj1VEuhgb',
            'spotify:playlist:37i9dQZF1DWU4xkXueiKGW',
            'spotify:playlist:37i9dQZF1DWUQru3jd69v5',
            'spotify:playlist:37i9dQZF1DXdhDukKQ88Cc',
            'spotify:playlist:37i9dQZF1DX0XUsuxWHRQd',
            'spotify:playlist:0mW4R77jxPXSrkH6NqFIkk'],

        'Jazz: average BMP range = 60 - 120': [
            'spotify:playlist:37i9dQZF1DX4wta20PHgwo',
            'spotify:playlist:37i9dQZF1DWVqfgj8NZEp1',
            'spotify:playlist:37i9dQZF1DXbITWG1ZJKYt',
            'spotify:playlist:37i9dQZF1DWVzZlRWgqAGH',
            'spotify:playlist:37i9dQZF1DXdwTUxmGKrdN',
            'spotify:playlist:37i9dQZF1DX2vYju3i0lNX'],

        'EDM: average BPM range = 120 - 180': [
            'spotify:playlist:37i9dQZF1DXaXB8fQg7xif',
            'spotify:playlist:37i9dQZF1DX4dyzvuaRJ0n',
            'spotify:playlist:37i9dQZF1DX32NsLKyzScr',
            'spotify:playlist:37i9dQZF1DWZ5Se2LB1C5h',
            'spotify:playlist:37i9dQZF1DX0BcQWzuB7ZO',
            'spotify:playlist:37i9dQZF1DX0HRj9P7NxeE'],

        'HipHop: average BPM ranage = 80 - 115': [
            'spotify:playlist:37i9dQZF1DWY4xHQp97fN6',
            'spotify:playlist:37i9dQZF1DWTggY0yqBxES',
            'spotify:playlist:37i9dQZF1DX2RxBh64BHjQ',
            'spotify:playlist:37i9dQZF1DX6GwdWRQMQpq',
            'spotify:playlist:37i9dQZF1DX186v583rmzp',
            'spotify:playlist:37i9dQZF1DX4ezQVslkJiT'],

        'Calm: average BPM = 70 - 110': [
            'spotify:playlist:37i9dQZF1DX1s9knjP51Oa',
            'spotify:playlist:37i9dQZF1DXaImRpG7HXqp',
            'spotify:playlist:37i9dQZF1DX5bjCEbRU4SJ',
            'spotify:playlist:37i9dQZF1DX9j444F9NCBa',
            'spotify:playlist:37i9dQZF1DWWTdxbiocWOL',
            'spotify:playlist:37i9dQZF1DXcr2UzLGERUU'],

        'IndieRock: average BPM range = 100 - 130': [
            'spotify:playlist:37i9dQZF1DX35DWKgAk2B5',
            'spotify:playlist:37i9dQZF1DWWEcRhUVtL8n',
            'spotify:playlist:37i9dQZF1DX26DKvjp0s9M',
            'spotify:playlist:37i9dQZF1DWUoqEG4WY6ce',
            'spotify:playlist:37i9dQZF1DXaRL7xbcDl7X',
            'spotify:playlist:37i9dQZF1DXdbXrPNafg9d'],

        'Instrumental: average BPM range = 85 - 125': [
            'spotify:playlist:37i9dQZF1DWWQRwui0ExPn',
            'spotify:playlist:37i9dQZF1DXa2SPUyWl8Y5',
            'spotify:playlist:37i9dQZF1DX692WcMwL2yW',
            'spotify:playlist:37i9dQZF1DX8Uebhn9wzrS',
            'spotify:playlist:37i9dQZF1DWYoYGBbGKurt',
            'spotify:playlist:37i9dQZF1DX8NTLI2TtZa6'],

        'Any genere': ['spotify:playlist:6aeG8saQTRQRdOmU2fPpj6',
                       'spotify:playlist:37i9dQZF1DXcBWIGoYBM5M',
                       'spotify:playlist:37i9dQZF1DX9oegrjMzKDW',
                       'spotify:playlist:37i9dQZF1DWYJ5kmTbkZiz',
                       'spotify:playlist:5SXcJ2VW1koQSEiItpMnZ3',
                       'spotify:playlist:37i9dQZF1DX4UtSsGT1Sbe']
        }

    return playlists[key][counter]
