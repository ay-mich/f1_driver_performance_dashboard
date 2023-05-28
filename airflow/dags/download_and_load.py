from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from airflow.utils.dates import days_ago
import pandas as pd
from sqlalchemy import create_engine
import requests
import os
import zipfile
import re

default_args = {
    "start_date": days_ago(0),
    "retries": 1,
}

dag = DAG(
    "download_and_load",
    default_args=default_args,
    description="Load Ergast F1 csv files into Postgres",
    schedule_interval=None,
)


def download_and_extract():
    url = "https://ergast.com/downloads/f1db_csv.zip"
    file_raw = "f1db_csv.zip"
    extract_folder = "./data/ergast/"

    # Download the file
    with open(file_raw, "wb") as f:
        r = requests.get(url)
        f.write(r.content)

    # Unzip the file
    with zipfile.ZipFile(file_raw, "r") as zip_ref:
        zip_ref.extractall(extract_folder)

    # remove the .zip file
    os.remove(file_raw)


t1 = PythonOperator(
    task_id="download_and_extract_file",
    python_callable=download_and_extract,
    dag=dag,
)


def camel_to_snake(name):
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


def load_csv_to_postgres():
    # Create a SQL Alchemy engine
    engine = create_engine("postgresql+psycopg2://f1_user:passwordf1@db/f1")

    # Folder where the CSVs are stored
    folder_path = "./data/ergast/"

    # Loop through each CSV file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            # Get the name of the table from the filename
            table_name = filename[:-4]
            # Load the CSV to a pandas dataframe, replace '\N' with NaN
            df = pd.read_csv(folder_path + filename, na_values=[r"\N"])

            # Convert column names from camelCase to snake_case
            df.columns = [camel_to_snake(col) for col in df.columns]

            # Write the dataframe to PostgreSQL
            df.to_sql(table_name, engine, if_exists="replace")


t2 = PythonOperator(
    task_id="load_data_to_postgres",
    python_callable=load_csv_to_postgres,
    dag=dag,
)

trigger_dbt_run = TriggerDagRunOperator(
    task_id="trigger_dbt_run",
    trigger_dag_id="dbt_runner",
    dag=dag,
)

t1 >> t2 >> trigger_dbt_run
