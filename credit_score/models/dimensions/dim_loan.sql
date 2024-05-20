{{ config(materialized='table') }}

SELECT
    LoanID,
    CustomerID,
    LoanAmount,
    InterestRate,
    LoanTerm,
    LoanStartDate,
    LoanEndDate,
    Status
FROM {{ ref('staging_loans') }};