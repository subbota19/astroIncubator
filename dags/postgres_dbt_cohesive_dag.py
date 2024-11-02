from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from os import environ, path
from datetime import datetime

AIRFLOW_HOME = environ.get("AIRFLOW_HOME")
DBT_PROFILE = environ.get("DBT_PROFILE")
TARGET_NAME = environ.get("TARGET_NAME")
DBT_PATH = environ.get("DBT_PATH")
VENV_PATH = "dbt_venv/bin/dbt"

profile_config = ProfileConfig(
    profile_name=DBT_PROFILE,
    target_name=TARGET_NAME,
    profiles_yml_filepath=f"{DBT_PATH}/profiles.yml"
)

project_config = ProjectConfig(
    dbt_project_path=DBT_PATH,
)

execution_config = ExecutionConfig(
    dbt_executable_path=f"{AIRFLOW_HOME}/{VENV_PATH}",
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
