from datetime import datetime, timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from airflow.providers.sqlite.operators.sqlite import SqliteOperator

from airflow.providers.sqlite.hooks.sqlite import SqliteHook
# https://airflow.apache.org/docs/apache-airflow/1.10.14/_api/airflow/hooks/dbapi_hook/index.html

def insert(**kwargs):
    import pandas as pd
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)
    sqlite_hook = SqliteHook(sqlite_conn_id='sqlite_default')
    connection = sqlite_hook.get_conn()    
    df.to_sql('df_table', con=connection, if_exists='append')


with DAG(
    'sozykin_sqlite_df',
    start_date=datetime(2023, 8, 5),
    schedule_interval='@daily'
) as dag:
    insert_data_from_df = PythonOperator(
        task_id='insert_data_from_df',
        python_callable=insert,
    )

    print_rows = SqliteOperator(
        task_id='print_rows',
        sqlite_conn_id='sqlite_default',
        sql='SELECT * from df_table'
    )

    insert_data_from_df >> print_rows