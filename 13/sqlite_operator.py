from datetime import datetime, timedelta

from airflow import DAG
# Подключаем SQLiteOperator
from airflow.providers.sqlite.operators.sqlite import SqliteOperator


default_args = {
    'owner': 'sozykin',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


with DAG(
    dag_id='dag_with_SQLite_operator',
    default_args=default_args,
    start_date=datetime(2023, 7, 18),
    schedule_interval='@daily'
) as dag:
    task1 = SqliteOperator(
        task_id='create_table',
        # Название соединения в AirFlow
        sqlite_conn_id='sqlite_aiflow_demo',
        sql="""
            CREATE TABLE IF NOT EXISTS dag_runs (
                dt date,
                dag_id character varying,
                primary key (dt, dag_id)
            )
        """
    )

    task2 = SqliteOperator(
        task_id='insert_into_table',
        # Название соединения в AirFlow
        sqlite_conn_id='sqlite_aiflow_demot',
        sql="""
            INSERT INTO dag_runs (dt, dag_id) VALUES ('{{ ds }}', '{{ dag.dag_id }}')
        """
    )

    task3 = SqliteOperator(
        task_id='delete_data_from_table',
        # Название соединения в AirFlow
        sqlite_conn_id='sqlite_aiflow_demo',
        sql="""
            DELETE FROM dag_runs WHERE dt = '{{ ds }}' AND dag_id = '{{ dag.dag_id }}';
        """
    )


    task1 >> task3 >> task2