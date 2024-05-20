{{ config(materialized='table') }}

SELECT
    OfficerID,
    Name,
    ContactInfo,
    BranchID
FROM {{ ref('staging_loan_officers') }};