import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


CLIENT_ID: str = os.environ.get('CLIENT_ID')
CLIENT_SECRET: str = os.environ.get('CLIENT_SECRET')

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
SPOTIFY_CLIENT = spotipy.Spotify(client_credentials_manager = client_credentials_manager)