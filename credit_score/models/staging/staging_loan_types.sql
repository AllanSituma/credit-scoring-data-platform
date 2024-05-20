{{ config(materialized='view') }}

SELECT
    LoanTypeID,
    LoanTypeName,
    Description,
    InterestRateRange,
    MaxLoanAmount
FROM {{ source('staging', 'loan_types') }};