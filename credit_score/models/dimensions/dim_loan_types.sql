{{ config(materialized='table') }}

SELECT
    LoanTypeID,
    LoanTypeName,
    Description,
    InterestRateRange,
    MaxLoanAmount
FROM {{ ref('staging_loan_types') }};