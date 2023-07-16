from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'sozykin',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


def greet():
    print("Hello World!")

with DAG(
    default_args=default_args,
    dag_id='dag_with_python_operator',
    description='Our first dag using python operator',
    start_date=datetime(2023, 7, 15),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
    )

    task1
