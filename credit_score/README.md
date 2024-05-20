# Credit Scoring Data Platform - dbt Project

## Overview

The dbt (data build tool) project within the Credit Scoring Data Platform is responsible for modeling and transforming data in the MySQL warehouse database according to the Kimball data model. It leverages dbt's capabilities to define SQL-based transformations and relationships between tables, enabling the creation of a structured and optimized data warehouse.

## Folder Structure

```
dbt_project/
│
├── dbt_project.yml       # dbt project configuration file
├── profiles.yml          # dbt profiles configuration file
├── models/               # Directory for dbt models
│   ├── dimensions/       # Directory for dimension models
│   │   ├── dim_customer.sql     # Dimension model for customer dimension
│   │   ├── dim_loan.sql         # Dimension model for loan dimension
│   │   ├── ...                  # Other dimension models
│   ├── facts/            # Directory for fact models
│   │   └── fact_loan.sql        # Fact model for loan fact table
│   ├── staging/          # Directory for staging models (optional)
│   │   ├── staging_customers.sql
│   │   ├── staging_loans.sql
│   │   ├── ...                  # Other staging models
│   └── README.md         # README file for dbt models
│
└── README.md             # README file for the dbt project
```

## dbt Project Configuration

- **dbt_project.yml**: This file contains the configuration settings for the dbt project, including the project name, version, and directories where dbt will look for models, tests, and snapshots.

- **profiles.yml**: The profiles.yml file contains the connection details for different environments (e.g., development, production) and defines how dbt should connect to your data warehouse.

## Models

- **Dimensions**: Dimension models represent entities such as customers, loans, loan officers, branches, etc. These models contain attributes and descriptive information about these entities.

- **Facts**: Fact models represent measurable metrics or events, such as loan transactions. They typically contain numerical values that can be aggregated and analyzed.

- **Staging** (optional): Staging models represent raw or unprocessed data ingested into the data warehouse. They serve as an intermediate step before transformation and modeling.

## Usage

1. **Compile Models**: Run `dbt compile` to compile the dbt project and generate SQL files for each model.

2. **Run Models**: Execute `dbt run` to execute the compiled SQL files and apply transformations to the data in the data warehouse.

3. **Test Models**: Use `dbt test` to run tests defined in your dbt project to ensure data quality and accuracy.

## Contributing

Contributions to this dbt project are welcome! Please feel free to submit issues, feature requests, or pull requests.

## License

This project is licensed under the [MIT License](../LICENSE).
