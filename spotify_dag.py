from airflow import DAG
from airflow.operators.python import PythonOperator

from spotify import extract_spotify_data, transform_spotify_data, load_transformed_spotify_data




with DAG(
    "etl_sales_daily",
    start_date="",
    schedule_interval=None,
) as dag:

    extract_data = PythonOperator(
        task_id="extract_data",
        python_callable = extract_spotify_data,   
        dag=dag,  
    )
    trasform_data = PythonOperator(
        task_id="transform_data",
        python_callable = transform_spotify_data,
        dag=dag
    )
    load_data = PythonOperator(
        task_id="load_data",
        python_callable = load_transformed_spotify_data,
        dag=dag
    )
   
    extract_data >> trasform_data >> load_data
