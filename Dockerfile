FROM quay.io/astronomer/astro-runtime:12.2.0

ENV DBT_PATH=/usr/local/airflow/dbt

RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip install --no-cache-dir dbt-duckdb dbt-postgres && deactivate

USER root

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         git bash nano \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY dbtHub/models/ $DBT_PATH/models/
COPY dbtHub/tests/ $DBT_PATH/tests/
COPY dbtHub/dbt_project.yml $DBT_PATH/
COPY dbtHub/profiles.yml $DBT_PATH/
COPY dbtHub/packages.yml $DBT_PATH/

ENV DBT_PROFILE postgres
ENV TARGET_NAME dev
