{{ config(materialized='table') }}

SELECT
    l.LoanID,
    l.CustomerID,
    l.LoanAmount,
    l.InterestRate,
    l.LoanTerm,
    l.LoanStartDate,
    l.LoanEndDate,
    l.Status,
    lo.OfficerID,
    b.BranchID,
    lt.LoanTypeID
FROM {{ ref('staging_loans') }} l
JOIN {{ ref('staging_loan_officers') }} lo ON l.OfficerID = lo.OfficerID
JOIN {{ ref('staging_branches') }} b ON l.BranchID = b.BranchID
JOIN {{ ref('staging_loan_types') }} lt ON l.LoanTypeID = lt.LoanTypeID;