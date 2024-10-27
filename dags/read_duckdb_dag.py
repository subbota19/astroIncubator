from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from os import makedirs, path
import duckdb


def read_duckdb_file():
    db_path = '/usr/local/airflow/db'

    if not path.exists(db_path):
        makedirs(db_path)
    con = duckdb.connect(database=f"{db_path}/sales.duckdb", read_only=False)

    con.sql("CREATE TABLE IF NOT EXISTS test (i INTEGER)")
    con.sql("INSERT INTO test VALUES (44)")
    con.table("test").show()

    con.close()


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG(
        dag_id='read_duckdb_dag',
        default_args=default_args,
        schedule_interval=None,
        catchup=False
) as dag:
    read_duckdb_task = PythonOperator(
        task_id='read_write_duckdb',
        python_callable=read_duckdb_file
    )

read_duckdb_task
