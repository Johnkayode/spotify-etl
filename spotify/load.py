from airflow.decorators import task


@task()
def load_transformed_spotify_data(data: list) -> list:
    print("Loading %d track(s) into the data warehouse" % len(data))
    return data