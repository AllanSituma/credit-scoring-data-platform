{{ config(materialized='view') }}

SELECT
    LoanID,
    CustomerID,
    LoanAmount,
    InterestRate,
    LoanTerm,
    LoanStartDate,
    LoanEndDate,
    Status,
    OfficerID,
    BranchID,
    LoanTypeID
FROM {{ source('staging', 'loans') }};