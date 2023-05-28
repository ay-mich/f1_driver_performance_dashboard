# F1 Driver Performance Dashboard

The F1 Driver Performance Dashboard is a powerful data visualization solution that enables users to track and analyze the performance of Formula 1 drivers over time. It leverages Docker for easy setup, Apache Airflow for data pipeline orchestration, PostgreSQL as the database, dbt (Data Build Tool) for data transformation, and Streamlit for interactive visualization.

## Prerequisites

You need to have Docker installed on your machine to run this project.

## Tech stack

To get started, you will need to install the following dependencies:

- Python 3.8+
- Streamlit
- PostgreSQL

## Features

The dashboard includes the following features:

- Driver selection: Users can select a driver to view their performance.
- Cumulative points: Shows the cumulative points for the selected driver.
- Relative performance: Shows the relative performance of the selected driver against their team mate(s).

## Getting Started

1. Clone the Repository
   First, clone this repository on your local machine by running the following command:

   `git clone <repository_url>`

2. Navigate to the Project Directory
   Change your current directory to the project directory:

   `cd f1_driver_performance_dashboard`

3. Build and Start the Docker Services
   You can build and start the services using docker-compose. Run the following command to do so:

   `docker-compose up --build`

   This will start two services:

- db: This is the PostgreSQL database service.
- airflow: This service runs Apache Airflow.
  It may take a few minutes to build the images and start the services. Once they are up, you can access the Airflow UI at http://localhost:8080.

4. Trigger the Data Pipeline
   Go to the Airflow UI and trigger the download_and_load DAG manually. This will download CSV data from https://ergast.com/downloads/f1db_csv.zip and load it into the Postgres database. The loaded data will then be transformed using dbt.

5. View the Dashboard
   The Streamlit dashboard is accessible at http://localhost:8501. Here you can select a driver from the dropdown menu and view their performance metrics.

## Data Source

The dashboard utilizes data derived from the comprehensive Ergast F1 API. The API provides an extensive variety of data about F1 drivers, including race results, lap times, and qualifying positions.

## Contributing

We welcome all contributions that improve the quality and functionality of this project. Please feel free to open a pull request with your proposed changes.

## License

This project is licensed under the MIT License, which allows for flexibility and widespread usage.

Should you have any questions or need further clarification, please don't hesitate to reach out. Happy coding!
