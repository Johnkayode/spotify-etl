import pandas as pd
from airflow.decorators import task

from spotify import SPOTIFY_CLIENT as spotify_client
from spotipy import Spotify

from spotify.schema import Artist, Track


@task()
def transform_spotify_data(tracks: list, client: Spotify=spotify_client) -> None:
    print("Received %d track(s): " % len(tracks))

    track_list = []
    artist_list = []
    for track in tracks:
        track = Track(track)
        track_list.append(track.__to_dict__)

        artist_details: dict = client.artist(track.lead_artist_id)
        artist = Artist(artist_details)
        artist_list.append(artist.__to_dict__)

    # copy last added tracks to file
    track_df = pd.DataFrame.from_dict(track_list)
    track_df = track_df.sort_values("played_at", ascending=True)
    track_df.to_csv(f"spotify/data/tracks.csv", index=False)

    # copy last added artists to file
    artist_df = pd.DataFrame.from_dict(artist_list)
    artist_df.to_csv(f"spotify/data/artists.csv", index=False)

    return {"tracks": track_list, "artists": artist_list}




