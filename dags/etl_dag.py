# dags/etl_dag.py
import subprocess
# from dotenv import load_dotenv

# This should be placed in the same folder as where airflow is installed.
# Hack: Create a symbolic link for this file, to where airflow is installed

# This achieves two things:
# 1. Allow airflow to detect this file
# 2. Allow this python file to remain in this project here, and easily import the run_pipeline callable in the project
from datetime import datetime, timedelta
from typing import Any
from airflow import DAG
from airflow.operators.python import PythonOperator

# This is not meant to be executed as a standalone script
# It is read and parsed by the Airflow Scheduler

# load_dotenv()
def run_non_rt_etl_pipeline() -> None:
    # TODO: Make Crypto Non RT ETL Pipeline to a Python Executable (PEX)
    # TODO: Make this compatible with Docker
    path_to_virtual_env = "/Users/eugeneleejunping/Documents/copies/crypto_non_rt_etl_pipeline/.venv/bin/python"
    path_to_entrypoint = "/Users/eugeneleejunping/Documents/copies/crypto_non_rt_etl_pipeline/src/chain_stack_eth_block_etl_pipeline.py"
    subprocess.run([path_to_virtual_env, path_to_entrypoint])


# Default arguments for the DAG
default_args: dict[str, Any] = {
    "owner": "airflow",
    "depends_on_past": False,  # each task instance runs independently of previous task instance
    "start_date": datetime(2024, 11, 12, 0, 0),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 5,
    "retry_delay": timedelta(minutes=5),
}

# Define the DAG
dag: DAG = DAG(
    "crypto_non_rt_etl_pipeline",
    description="ETL pipeline to run crypto_non_rt_etl_pipeline",
    default_args=default_args,
    schedule_interval=timedelta(days=1),
)

# Define the first task to process the first dataset
task1: PythonOperator = PythonOperator(
    task_id="run_etl_pipeline",
    python_callable=run_non_rt_etl_pipeline,
    op_kwargs={},
    dag=dag,
)

if __name__ == "__main__":
    run_non_rt_etl_pipeline()
