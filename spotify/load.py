from airflow.decorators import task
from airflow.providers.postgres.hooks.postgres import PostgresHook

from spotify.sql.utils import create_track, get_or_create_artist

@task()
def load_transformed_spotify_data(data: dict) -> list:
    recently_played_tracks = data["tracks"]
    artists = data["artists"]

    hook = PostgresHook()
   
    for track in recently_played_tracks:
        artist = next((artist for artist in artists if artist["id"] == track["lead_artist_id"]), None)
        try:
            sql = get_or_create_artist(artist)
            artist_id = hook.get_first(sql)
            if artist_id and artist_id[0] is not None:
                sql, values = create_track(track, artist_id[0])
                hook.run(sql, parameters=values)
        except Exception as e:
            raise e
       
            