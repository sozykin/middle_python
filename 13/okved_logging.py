from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import json
import logging

default_args = {
    'owner': 'sozykin',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


def read_json():
    logger = logging.getLogger(__name__)
    with open("/home/andrey/okved_2.json", "r") as read_file:
        data = json.load(read_file)
        logger.info("Данные из файла загружены")
        print(data[:2])

 

with DAG(
    dag_id='download_okved',
    default_args=default_args,
    description='DAG for donwload okved file',
    start_date=datetime(2023, 7, 15, 8),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='download_file',
        bash_command="wget https://ofdata.ru/open-data/download/okved_2.json.zip -O /home/andrey/okved_2.json.zip"
    )

    task2 = BashOperator(
        task_id='unzip_file',
        bash_command="unzip -o /home/andrey/okved_2.json.zip -d /home/andrey/"
    )
    task3 = PythonOperator(
        task_id='parse',
        python_callable=read_json,
    )



    task1 >> task2 >> task3
