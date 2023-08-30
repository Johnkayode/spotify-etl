from airflow.decorators import task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime
from spotify import SPOTIFY_CLIENT as spotify_client
from spotify.sql.utils import retrieve_last_played_at
from spotipy import Spotify



def convert_dt_to_timestamp(dt: datetime) -> int:
    timestamp = int(dt.timestamp()) * 1000 + dt.microsecond // 1000
    return timestamp


@task
def extract_spotify_data(client: Spotify=spotify_client) -> list:
    """
    Extract data from Spotify
    """
    hook = PostgresHook()

    # retrieve timestamp of last played track from the database
    sql = retrieve_last_played_at()
    res = hook.get_first(sql)
    last_timestamp = res[0] if res and res[0] is not None else None
    last_timestamp = convert_dt_to_timestamp(last_timestamp) if last_timestamp else None

    resp: dict = client.current_user_recently_played(limit=50, after=last_timestamp)
    tracks: list = resp.get("items")

    print("%d track(s) retrieved from Spotify" % len(tracks))
    return tracks

