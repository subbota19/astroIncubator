"""
Test PostgreSQL Connection DAG
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from os import path
from datetime import datetime


def test_postgres_connection():
    hook = PostgresHook(postgres_conn_id="postgres_default")
    result = hook.get_first("SELECT 1;")
    return result


default_args = {
    "owner": "airflow",
    "start_date": datetime(2023, 1, 1),
    "retries": 1,
}

with DAG(
        dag_id=path.splitext(path.basename(__file__))[0],
        default_args=default_args,
        schedule_interval=None,
        catchup=False,
        doc_md=__doc__,
) as dag:
    test_connection = PythonOperator(
        task_id="test_postgres_connection_task",
        python_callable=test_postgres_connection,
    )
