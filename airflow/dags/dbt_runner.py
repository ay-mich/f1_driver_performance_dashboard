from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from airflow import DAG

default_args = {
    "start_date": days_ago(0),
    "retries": 1,
}

dag = DAG(
    "dbt_runner",
    default_args=default_args,
    description="Running DBT debug, clean and run on models",
    schedule_interval=None,
)

debug_dbt = BashOperator(
    task_id="debug_dbt",
    bash_command="cd /opt/modeling && dbt debug",
    dag=dag,
)

clean_dbt = BashOperator(
    task_id="clean_dbt",
    bash_command="cd /opt/modeling && dbt clean",
    dag=dag,
)

run_dbt = BashOperator(
    task_id="run_dbt",
    bash_command="cd /opt/modeling && dbt run",
    dag=dag,
)

debug_dbt >> clean_dbt >> run_dbt
