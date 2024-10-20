FROM quay.io/astronomer/astro-runtime:12.2.0

ENV DBT_PATH=/usr/local/airflow/dbt/duckdb/

RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip install --no-cache-dir dbt-duckdb && deactivate

USER root

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         git bash nano \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN git clone --no-checkout https://github.com/subbota19/dbtAstro.git $DBT_PATH && \
    cd $DBT_PATH && \
    git config core.sparseCheckout true && \
    echo "models/*" >> .git/info/sparse-checkout && \
    echo "tests/*" >> .git/info/sparse-checkout && \
    echo "dbt_project.yml" >> .git/info/sparse-checkout && \
    echo "profiles.yml" >> .git/info/sparse-checkout && \
    echo "packages.yml" >> .git/info/sparse-checkout && \
    git checkout main

