from datetime import datetime, timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

from airflow.providers.postgres.hooks.postgres import PostgresHook
# https://airflow.apache.org/docs/apache-airflow/1.10.14/_api/airflow/hooks/dbapi_hook/index.html

def insert(**kwargs):
    import pandas as pd
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)
    postgres_hook = PostgresHook(postgres_conn_id='postgres_localhost')
    engine = postgres_hook.get_sqlalchemy_engine()    
    df.to_sql('df_table', con=engine, if_exists='append')


with DAG(
    'sozykin_postgresql_df',
    start_date=datetime(2023, 8, 5),
    schedule_interval='@daily'
) as dag:
    insert_data_from_df = PythonOperator(
        task_id='insert_data_from_df',
        python_callable=insert,
    )

    print_rows = PostgresOperator(
        task_id='print_rows',
        postgres_conn_id='postgres_localhost',
        sql='SELECT * from df_table'
    )

    insert_data_from_df >> print_rows