{{ config(materialized='view') }}

SELECT
    CustomerID,
    Name,
    Address,
    ContactInfo
FROM {{ source('staging', 'customers') }};