from airflow import DAG
from airflow.decorators import dag
import pendulum

from spotify import extract_spotify_data, transform_spotify_data, load_transformed_spotify_data



@dag(
    dag_id="spotify_etl",
    schedule_interval="@daily",
    start_date=pendulum.datetime(2023, 7, 25, 8, 0, 0),
    catchup=False
)
def spotify_etl():
    spotify_data = extract_spotify_data()
    transformed_data = transform_spotify_data(spotify_data)
    load_data = load_transformed_spotify_data(transformed_data)

    spotify_data >> transformed_data >> load_data
   

spotify_etl_dag = spotify_etl()
