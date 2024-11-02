from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig, RenderConfig
from os import environ, path
from datetime import datetime

AIRFLOW_HOME = environ.get("AIRFLOW_HOME")
DBT_PROFILE = environ.get("DBT_PROFILE")
TARGET_NAME = environ.get("TARGET_NAME")
DBT_PATH = environ.get("DBT_PATH")
DBT_TAGS = ["staging", "core", "data_products"]
VENV_PATH = "dbt_venv/bin/dbt"


def create_dbt_dag(layer_tag: str):
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
    render_config = RenderConfig(
        select=[f"tag:{layer_tag}"],
        exclude=["tag:test"]
    )
    default_args = {
        "retries": 2
    }
    dag_id = f"{path.splitext(path.basename(__file__))[0]}_{layer_tag}"

    dbt_dag = DbtDag(
        project_config=project_config,
        profile_config=profile_config,
        execution_config=execution_config,
        render_config=render_config,
        schedule_interval=None,
        operator_args={
            "install_deps": True
        },
        start_date=datetime(2023, 1, 1),
        catchup=False,
        dag_id=dag_id,
        default_args=default_args,
    )
    globals()[dag_id] = dbt_dag


for tag in DBT_TAGS:
    create_dbt_dag(layer_tag=tag)
