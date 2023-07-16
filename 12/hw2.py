from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'sozykin',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    dag_id='Hello_world_DAG_v2',
    default_args=default_args,
    description='This is our first dag that we write',
    start_date=datetime(2023, 7, 15, 8),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo Hello World from task1!"
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo Hello World from task2!"
    )

    task1.set_downstream(task2)
