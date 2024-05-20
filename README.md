# Credit Scoring Data Platform

## Overview

The Credit Scoring Data Platform is a comprehensive solution for managing and analyzing credit-related data. It includes components for data extraction, transformation, loading, modeling, and visualization, enabling organizations to gain insights into customer behavior, loan performance, and more.

## Components

### 1. MySQL Databases
- **MySQL Warehouse Database**: Stores transformed and modeled data for analysis.
- **MySQL Production Database**: Contains production data from which information is extracted.

### 2. Python ETL Scripts
- **generate_data.py**: Python script to generate sample data for testing and development.
- **etl_script.py**: Python script to extract data from the production database, transform it, and load it into the warehouse database.

### 3. dbt (Data Build Tool) Project
- A dbt project to model and transform data in the warehouse database according to the Kimball data model.

### 4. Docker Compose Configuration
- Docker Compose file to set up and orchestrate the entire data platform environment.

## Setup and Usage

1. **Clone Repository**: Clone this repository to your local machine.
2. **Environment Variables**: Set up necessary environment variables for database connections and configurations. Update the `.env` file with your credentials.
3. **Docker**: Ensure Docker is installed on your system.
4. **Build Docker Images**: Run `docker-compose build` to build the Docker images.
5. **Start Containers**: Run `docker-compose up -d` to start the containers in detached mode.
6. **Execute ETL**: The Python ETL scripts and dbt project will automatically run when the containers start. Check logs for any errors.
7. **Access Data**: Once the containers are running, you can access the MySQL warehouse database to analyze the transformed data.
8. **Customization**: Modify the ETL scripts, dbt models, and Docker configurations as needed to fit your specific requirements.

## Contributing

Contributions to this project are welcome! Please feel free to submit issues, feature requests, or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

