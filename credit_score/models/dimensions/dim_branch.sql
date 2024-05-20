{{ config(materialized='table') }}

SELECT
    BranchID,
    BranchName,
    Location,
    ContactInfo
FROM {{ ref('staging_branches') }};