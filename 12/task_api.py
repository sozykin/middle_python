from datetime import datetime, timedelta
from airflow.decorators import dag, task


default_args = {
    'owner': 'sozykin',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

@dag(dag_id='dag_with_taskflow_api',
     default_args=default_args,
     start_date=datetime(2023, 7, 16),
     schedule_interval='@daily')
def hello_world_etl():

    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name': 'Андрей',
            'last_name': 'Созыкин'
        }

    @task()
    def get_age():
        return 44

    @task()
    def greet(first_name, last_name, age):
        print(f"Привет! Меня зовут {first_name} {last_name}, мой возраст: {age}")


    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict['first_name'],
          last_name=name_dict['last_name'],
          age=age)

greet_dag = hello_world_etl()