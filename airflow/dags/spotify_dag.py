from airflow.decorators import dag
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.dates import days_ago

from spotify import extract_spotify_data, transform_spotify_data, load_transformed_spotify_data



@dag(
    dag_id="spotify_etl",
    schedule_interval="@daily",
    start_date=days_ago(1),
    catchup=False
)
def spotify_etl():
    create_tables = PostgresOperator(
        sql="sql/create_tables.sql",
        task_id="create_tables"
    )
    spotify_data = extract_spotify_data()
    transformed_data = transform_spotify_data(spotify_data)
    load_data = load_transformed_spotify_data(transformed_data)


    create_tables >> spotify_data >> transformed_data >> load_data
   

spotify_etl_dag = spotify_etl()
