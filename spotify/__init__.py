import spotipy
from decouple import config
from spotipy.oauth2 import SpotifyClientCredentials


CLIENT_ID: str = config('CLIENT_ID')
CLIENT_SECRET: str = config('CLIENT_SECRET')

client_credentials_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID, 
    client_secret=CLIENT_SECRET,
    scope="playlist-read-private,playlist-read-collaborative"
)
SPOTIFY_CLIENT = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


from .extract import *
from .transform import *
from .load import *