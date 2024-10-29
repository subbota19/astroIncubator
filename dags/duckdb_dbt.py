from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from os import environ, path
from datetime import datetime

AIRFLOW_HOME = environ['AIRFLOW_HOME']

profile_config = ProfileConfig(
    profile_name="duckdb",
    target_name="dev",
    profiles_yml_filepath="/usr/local/airflow/dbt/duckdb/profiles.yml"
)

project_config = ProjectConfig(
    dbt_project_path="/usr/local/airflow/dbt/duckdb",
)

execution_config = ExecutionConfig(
    dbt_executable_path=f"{AIRFLOW_HOME}/dbt_venv/bin/dbt",
)

duckdb_dag = DbtDag(
    project_config=project_config,
    profile_config=profile_config,
    execution_config=execution_config,
    schedule_interval="@daily",
    operator_args={
        "install_deps": True
    },
    start_date=datetime(2023, 1, 1),
    catchup=False,
    dag_id=path.splitext(path.basename(__file__))[0],
    default_args={"retries": 2},
)
