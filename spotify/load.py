from airflow.decorators import task
from airflow.providers.postgres.hooks.postgres import PostgresHook

@task()
def load_transformed_spotify_data(data: dict) -> list:
    recently_played_tracks = data["tracks"]
    artists = data["artists"]

    hook = PostgresHook()
    with hook.get_conn() as connection:
        for track in recently_played_tracks:
            sql = f"INSERT INTO RecentlyPlayedTracks (track_id, track_name, artist_id, played_at) VALUES ('{row['track_id']}', '{row['track_name']}', {row['artist_id']}, '{row['played_at']}');"
            connection.run(sql)
            connection.commit()