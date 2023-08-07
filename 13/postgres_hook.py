from datetime import datetime, timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

from airflow.providers.postgres.hooks.postgres import PostgresHook
# https://airflow.apache.org/docs/apache-airflow/1.10.14/_api/airflow/hooks/dbapi_hook/index.html

def insert(**kwargs):
    exec_time = kwargs['ts']
    sqlite_hook = PostgresHook(postgres_conn_id='postgres_localhost')
    rows = [(1,  exec_time),]
    fields = ['id', 'exec_time']
    sqlite_hook.insert_rows(
        table='example',
        rows=rows,
        target_fields=fields,
    )

with DAG(
    'sozykin_postgresql',
    start_date=datetime(2023, 7, 18),
    schedule_interval='@daily'
) as dag:
    insert_into_example = PythonOperator(
        task_id='insert_into_example',
        python_callable=insert,
    )

    print_rows = PostgresOperator(
        task_id='print_rows',
        postgres_conn_id='postgres_localhost',
        sql='SELECT id, exec_time from example'
    )

    insert_into_example >> print_rows