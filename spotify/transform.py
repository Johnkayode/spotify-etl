import pandas as pd
from airflow.decorators import task

from spotify.schema import Track


#@task()
def transform_spotify_data(tracks: list) -> None:
    print("Received %d track(s): " % len(tracks))

    for track in tracks:
        track = Track(track)
        print(track)

    return None



import json

with open('result.json') as f:
    data = json.load(f)
    f.close()

tracks: list = data.get("items")
transform_spotify_data(tracks)


