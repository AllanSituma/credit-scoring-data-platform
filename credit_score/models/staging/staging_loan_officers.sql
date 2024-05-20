{{ config(materialized='view') }}

SELECT
    OfficerID,
    Name,
    ContactInfo,
    BranchID
FROM {{ source('staging', 'loan_officers') }};