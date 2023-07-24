import spotipy
from decouple import config
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth


USER_ID: str = config('USER_ID')
CLIENT_ID: str = config('CLIENT_ID')
CLIENT_SECRET: str = config('CLIENT_SECRET')
REDIRECT_URI: str = config('REDIRECT_URI')

# client_credentials_manager = SpotifyClientCredentials(
#     client_id=CLIENT_ID, 
#     client_secret=CLIENT_SECRET,
#     # scope="playlist-read-private,playlist-read-collaborative"
# )
   
auth_manager = SpotifyOAuth(
    scope="user-library-read,user-top-read,user-read-recently-played,playlist-read-private",
    username=USER_ID,
    redirect_uri=REDIRECT_URI,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)
SPOTIFY_CLIENT = spotipy.Spotify(auth_manager = auth_manager)


from .extract import *
from .transform import *
from .load import *