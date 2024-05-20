{{ config(materialized='view') }}

SELECT
    BranchID,
    BranchName,
    Location,
    ContactInfo
FROM {{ source('staging', 'branches') }};