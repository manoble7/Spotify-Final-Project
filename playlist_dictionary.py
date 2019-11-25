import spotipy

# Create dictionary with playlists to access given a particular genre parameter.

# These are all playlists made by Spotify and updated fairly regularly (?)
def get_playlist_ID(key):
    
    playlists = {
        'Classic Rock': 'spotify:playlist:37i9dQZF1DWXRqgorJj26U',  # Rock Classics
        'Pop': 'spotify:playlist:37i9dQZF1DXcBWIGoYBM5M',  # Todays Top Hits
        'R&B': 'spotify:playlist:37i9dQZF1DX4SBhb3fqCJd',  # Are & Be
        'Rap': 'spotify:playlist:37i9dQZF1DX0XUsuxWHRQd',  # RapCaviar
        'Jazz': 'spotify:playlist:37i9dQZF1DWVqfgj8NZEp1',  # Coffee Table Jazz
        'Country': 'spotify:playlist:37i9dQZF1DX1lVhptIYRda',  # Hot Country
        'EDM': 'spotify:playlist:37i9dQZF1DXaXB8fQg7xif',  # Dance Party
        'HipHop': 'spotify:playlist:37i9dQZF1DWY4xHQp97fN6',  # Get Turnt
        'Calm': 'spotify:playlist:37i9dQZF1DX1s9knjP51Oa',  # Calm Vibes
        'Indie Rock': 'spotify:playlist:37i9dQZF1DX2Nc3B70tvx0',  # Ultimate Indie
        'Instrumental': 'spotify:playlist:37i9dQZF1DWWQRwui0ExPn'  # Lo-fi Beats
    }
        
    return playlists[key]

