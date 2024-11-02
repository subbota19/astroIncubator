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

COPY dbtAstro/models/ $DBT_PATH/models/
COPY dbtAstro/tests/ $DBT_PATH/tests/
COPY dbtAstro/dbt_project.yml $DBT_PATH/
COPY dbtAstro/profiles.yml $DBT_PATH/
COPY dbtAstro/packages.yml $DBT_PATH/

#RUN git clone --no-checkout https://github.com/subbota19/dbtAstro.git $DBT_PATH && \
#    cd $DBT_PATH && \
#    git config core.sparseCheckout true && \
#    echo "models/*" >> .git/info/sparse-checkout && \
#    echo "tests/*" >> .git/info/sparse-checkout && \
#    echo "dbt_project.yml" >> .git/info/sparse-checkout && \
#    echo "profiles.yml" >> .git/info/sparse-checkout && \
#    echo "packages.yml" >> .git/info/sparse-checkout && \
#    git checkout main

ENV DBT_PROFILE postgres
ENV TARGET_NAME dev