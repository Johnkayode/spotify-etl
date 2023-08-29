from airflow.decorators import task
from datetime import datetime
from spotify import SPOTIFY_CLIENT as spotify_client
from spotipy import Spotify


@task
def extract_spotify_data(client: Spotify=spotify_client) -> list:
    """
    Extract data from Spotify
    """
    last_timestamp = datetime.today().timestamp()
    resp: dict = client.current_user_recently_played(limit=50) #after=last_timestamp
    tracks: list = resp.get("items")

    print("%d track(s) retrieved from Spotify" % len(tracks))
    return tracks

