from airflow.decorators import task


@task()
def load_transformed_spotify_data(data: dict) -> dict:
    pass