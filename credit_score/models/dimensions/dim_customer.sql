{{ config(materialized='table') }}

SELECT
    CustomerID,
    Name,
    Address,
    ContactInfo
FROM {{ ref('staging_customers') }};