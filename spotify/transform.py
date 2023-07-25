import pandas as pd
from airflow.decorators import task

@task()
def transform_spotify_data(data: list) -> None:
    print("Received %d track(s): " % len(data), data)
    return data