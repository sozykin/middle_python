from datetime import datetime, timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from airflow.providers.sqlite.operators.sqlite import SqliteOperator

from airflow.providers.sqlite.hooks.sqlite import SqliteHook
# https://airflow.apache.org/docs/apache-airflow/1.10.14/_api/airflow/hooks/dbapi_hook/index.html

def insert(**kwargs):
    exec_time = kwargs['ts']
    sqlite_hook = SqliteHook(sqlite_conn_id='sqlite_default')
    rows = [(1,  exec_time),]
    fields = ['id', 'exec_time']
    sqlite_hook.insert_rows(
        table='example',
        rows=rows,
        target_fields=fields,
    )

with DAG(
    'conhook',
    start_date=datetime(2023, 7, 18),
    schedule_interval='@daily'
) as dag:
    insert_into_example = PythonOperator(
        task_id='insert_into_example',
        python_callable=insert,
    )

    print_rows = SqliteOperator(
        task_id='print_rows',
        sqlite_conn_id='sqlite_default',
        sql='SELECT id, exec_time from example'
    )

    insert_into_example >> print_rows