from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'catchup': False
}

with DAG('test_dag2', default_args=default_args, schedule_interval='@daily') as dag:
    start = DummyOperator(task_id='start')

