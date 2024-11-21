# Airflow DAG files for crypto_non_rt_etl_pipeline_dag

## Steps to Install

```commandline
poetry shell
poetry install
```

Apache airflow installation is not support by poetry yet

To install:

TODO: move pip commands to requirements.txt

```commandline
pip install 'apache-airflow==2.10.3' \
 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.3/constraints-3.9.txt"
 
pip install psycopg2-binary==2.9.10
```

## The DAG file is separate from `crypto_non_rt_etl_pipeline` project

The ETL pipeline project has a dependency clash with apache-airflow; it uses `sqlalchemy = "^2.0.0"`

However, airflow requires `sqlalchemy =">=1.4.0,<2.0.0"`

To overcome this, we separated the DAG file definition in this project, away from the other project.

Then, the DAG file here runs the ETL project as a subprocess

## Symlink DAG file into airflow, so it can be detected

```commandline
ln -s /Users/eugeneleejunping/Documents/crypto_non_rt_etl_pipeline_dag/dags/etl_dag.py ~/airflow/dags/etl_dag.py
```

## Setup airflow

```commandline
# CHANGE THIS
export AIRFLOW_HOME=/Users/eugeneleejunping/airflow
airflow scheduler
```

```commandline
# CHANGE THIS
export AIRFLOW_HOME=/Users/eugeneleejunping/airflow
airflow webserver --port 8080
```

#### Create an Airflow Webserver credential

```commandline
export AIRFLOW_HOME=/Users/eugeneleejunping/airflow
airflow users create \
    --username admin \
    --password admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com
```