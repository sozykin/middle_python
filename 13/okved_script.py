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
    # Получаем текущий logger для модуля
    logger = logging.getLogger(__name__)
    with open("/home/andrey/okved_2.json", "r") as read_file:
        data = json.load(read_file)
        # Делаем запись в журнал
        logger.info("Данные из файла загружены")
        print(data[:2])

with DAG(
    dag_id='download_okved_script',
    default_args=default_args,
    description='DAG for donwload okved file',
    start_date=datetime(2023, 7, 15, 8),
                     # ┌───────────── Минуты (0 - 59)
                     # │ ┌───────────── Часы (0 - 23)
                     # │ │ ┌───────────── День месяца (1 - 31)
                     # │ │ │ ┌───────────── Месяц (1 - 12)
                     # │ │ │ │ ┌───────────── День недели (0 - 6) (воскресенье - суббота)
                     # │ │ │ │ │
                     # │ │ │ │ │
                     # │ │ │ │ │
    schedule_interval='0 0 * * *'
) as dag:
    task1 = BashOperator(
        task_id='download_file',
        bash_command="/home/andrey/projects/airflow/script.sh "
    )

    task2 = PythonOperator(
        task_id='parse',
        python_callable=read_json,
    )



    task1 >> task2