from airflow import DAG
from airflow.decorators import dag
from airflow.operators.python import PythonOperator

from spotify import extract_spotify_data, transform_spotify_data, load_transformed_spotify_data




@dag(
    dag_id="spotify_etl",
    schedule_interval="@daily",
    start_date="",
    catchup=False
)
def spotify_etl():
    data = extract_spotify_data()
    transformed_data = transform_spotify_data(data)
    load_transformed_spotify_data(transform_spotify_data)
    

