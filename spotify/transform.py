import pandas as pd
from airflow.decorators import task

@task()
def transform_spotify_data(data: dict) -> dict:
    print("Tracks: ", data)