from airflow.decorators import task
from airflow.providers.postgres.hooks.postgres import PostgresHook

from spotify.sql.utils import create_track, get_or_create_artist

@task()
def load_transformed_spotify_data(data: dict) -> list:
    recently_played_tracks = data["tracks"]
    artists = data["artists"]

    hook = PostgresHook()
    with hook.get_conn() as connection:
        for track in recently_played_tracks:
            artist_id = get_or_create_artist(track.lead_artist_id)
            sql = create_track(track, artist_id)
            connection.run(sql)
            connection.commit()