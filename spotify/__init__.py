import spotipy
from decouple import config
from spotify.auth import get_access_token


# client_credentials_manager = SpotifyClientCredentials(
#     client_id=CLIENT_ID, 
#     client_secret=CLIENT_SECRET,
#     # scope="playlist-read-private,playlist-read-collaborative"
# )
   
# auth_manager = SpotifyOAuth(
#     scope="user-library-read,user-top-read,user-read-recently-played,playlist-read-private",
#     username=USER_ID,
#     redirect_uri=REDIRECT_URI,
#     client_id=CLIENT_ID,
#     client_secret=CLIENT_SECRET
# )
SPOTIFY_CLIENT = spotipy.Spotify(auth=get_access_token())


from .extract import *
from .transform import *
from .load import *