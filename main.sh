#!/bin/bash

echo "Creating Airflow folder structure"
mkdir -p airflow/dags airflow/logs airflow/plugins
echo "Airflow folder structure created"

echo "Starting Database and Airflow"
docker-compose up -d
echo "Database and Airflow started"
