# astroIncubator

The astroIncubator repository is designed as a workspace for developing Airflow DAGs, with a focus on integrating the Compass framework for orchestrating dbt modules. The project includes:

1) Cohesive DAG: A single DAG orchestrating all dbt modules as one workflow.
2) Modular DAGs: Multiple sub-DAGs created dynamically using tags, allowing for targeted scheduling of specific dbt stages.

## Core Concepts

**Compass Framework**: The primary approach used for scheduling dbt models into structured DAGs.

**dbt Integration**: Using tags, the DAG can selectively run dbt tests and execute specific dbt workflows.

**PostgreSQL Backend**: All dbt setups, including metadata and configurations, are stored in a PostgreSQL.

**Git Submodule**: dbt code is located in [submodule](https://github.com/subbota19/dbtHub/tree/4389c30392810a6b421f2e67ec16ac3c69790db3)
