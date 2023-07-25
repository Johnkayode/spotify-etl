from airflow.decorators import task
from spotify import SPOTIFY_CLIENT as spotify_client
from spotipy import Spotify


@task
def extract_spotify_data(client: Spotify=spotify_client) -> list:
    """
    Extract data from Spotify
    """
    tracks: list = client.current_user_recently_played(limit=50)
    audio_features: list = client.audio_features(tracks=[])
    # audio_analysis = client.audio_analysis()
    # data = None
    
    print("%d track(s) retrieved from Spotify" % len(tracks))
    return tracks