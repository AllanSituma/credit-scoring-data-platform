import mysql.connector
import random
from datetime import datetime, timedelta

# Function to create a MySQL database and tables
def create_database():
    conn = mysql.connector.connect(
        host='mysql-production',
        user='root',
        password='password',
        database='loans_db'
    )
    cursor = conn.cursor()

    # Create Customers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customers (
            CustomerID INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(255),
            Address VARCHAR(255),
            ContactInfo VARCHAR(255)
        )
    ''')

    # Create Loans table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Loans (
            LoanID INT AUTO_INCREMENT PRIMARY KEY,
            CustomerID INT,
            LoanAmount DECIMAL(10, 2),
            InterestRate DECIMAL(5, 4),
            LoanTerm INT,
            LoanStartDate DATE,
            LoanEndDate DATE,
            Status VARCHAR(50),
            FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
        )
    ''')

    # Create Payments table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Payments (
            PaymentID INT AUTO_INCREMENT PRIMARY KEY,
            LoanID INT,
            PaymentAmount DECIMAL(10, 2),
            PaymentDate DATE,
            FOREIGN KEY (LoanID) REFERENCES Loans(LoanID)
        )
    ''')

    # Create LoanOfficers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS LoanOfficers (
            OfficerID INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(255),
            ContactInfo VARCHAR(255),
            BranchID INT,
            FOREIGN KEY (BranchID) REFERENCES Branches(BranchID)
        )
    ''')

    # Create Branches table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Branches (
            BranchID INT AUTO_INCREMENT PRIMARY KEY,
            BranchName VARCHAR(255),
            Location VARCHAR(255),
            ContactInfo VARCHAR(255)
        )
    ''')

    # Create LoanTypes table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS LoanTypes (
            LoanTypeID INT AUTO_INCREMENT PRIMARY KEY,
            LoanTypeName VARCHAR(255),
            Description TEXT,
            InterestRateRange VARCHAR(255),
            MaxLoanAmount DECIMAL(10, 2)
        )
    ''')

    # Create Documents table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Documents (
            DocumentID INT AUTO_INCREMENT PRIMARY KEY,
            LoanID INT,
            DocumentType VARCHAR(255),
            DocumentName VARCHAR(255),
            DocumentContent BLOB,
            FOREIGN KEY (LoanID) REFERENCES Loans(LoanID)
        )
    ''')

    conn.commit()
    conn.close()

# Function to generate random customer data
def generate_customer_data(num_customers):
    customer_data = []
    for customer_id in range(1, num_customers + 1):
        name = f'Customer {customer_id}'
        address = f'{random.randint(100, 999)} {random.choice(["Main", "Elm", "Maple"])} St'
        contact_info = f'customer{customer_id}@example.com'
        customer_data.append((name, address, contact_info))
    return customer_data

# Function to generate sample entries for loans
def generate_sample_loans(num_customers):
    loans_data = []
    for customer_id in range(1, num_customers + 1):
        num_loans = random.randint(1, 70)
        for _ in range(num_loans):
            loan_amount = random.uniform(1000, 10000)
            interest_rate = random.uniform(0.05, 0.1)
            loan_term = random.randint(12, 60)
            start_date = datetime(2020, 1, 1)
            loan_start_date = start_date.strftime('%Y-%m-%d')
            loan_end_date = (start_date + timedelta(days=loan_term * 30)).strftime('%Y-%m-%d')
            status = random.choices(['Active', 'Paid Off', 'Defaulted'], weights=[0.7, 0.2, 0.1])[0]
            loans_data.append((customer_id, loan_amount, interest_rate, loan_term, loan_start_date, loan_end_date, status))
    return loans_data

# Function to generate sample entries for loan officers
def generate_loan_officers(num_officers):
    officers_data = []
    for officer_id in range(1, num_officers + 1):
        name = f'Loan Officer {officer_id}'
        contact_info = f'officer{officer_id}@example.com'
        branch_id = random.randint(1, 10)  # Assuming there are 10 branches
        officers_data.append((name, contact_info, branch_id))
    return officers_data

# Function to generate sample entries for branches
def generate_branches(num_branches):
    branches_data = []
    for branch_id in range(1, num_branches + 1):
        branch_name = f'Branch {branch_id}'
        location = f'{random.choice(["Downtown", "Suburb", "City Center"])}'
        contact_info = f'branch{branch_id}@example.com'
        branches_data.append((branch_name, location, contact_info))
    return branches_data

# Function to generate sample entries for loan types
def generate_loan_types(num_loan_types):
    loan_types_data = []
    for loan_type_id in range(1, num_loan_types + 1):
        loan_type_name = f'Loan Type {loan_type_id}'
        description = f'Description for Loan Type {loan_type_id}'
        interest_rate_range = f'{random.uniform(0.05, 0.1)} - {random.uniform(0.1, 0.15)}'
        max_loan_amount = random.uniform(5000, 20000)
        loan_types_data.append((loan_type_name, description, interest_rate_range, max_loan_amount))
    return loan_types_data

if __name__ == "__main__":
    num_customers = 10000
    num_loan_officers = 50
    num_branches = 10
    num_loan_types = 5

    create_database()

    customer_data = generate_customer_data(num_customers)
    loans_data = generate_sample_loans(num_customers)
    officers_data = generate_loan_officers(num_loan_officers)
    branches_data = generate_branches(num_branches)
    loan_types_data = generate_loan_types(num_loan_types)

    conn = mysql.connector.connect(
        host='mysql-production',
        user='root',
        password='password',
        database='loans_db'
    )
    cursor = conn.cursor()

    # Insert customer data into Customers table
    cursor.executemany('INSERT INTO Customers (Name, Address, ContactInfo) VALUES (%s, %s, %s)', customer_data)

    # Insert loan data into Loans table
    cursor.executemany('INSERT INTO Loans (CustomerID, LoanAmount, InterestRate, LoanTerm, LoanStartDate, LoanEndDate, Status) VALUES (%s, %s, %s, %s, %s, %s, %s)', loans_data)

    # Insert loan officer data into LoanOfficers table
    cursor.executemany('INSERT INTO LoanOfficers (Name, ContactInfo, BranchID) VALUES (%s, %s, %s)', officers_data)

    # Insert branch data into Branches table
    cursor.executemany('INSERT INTO Branches (BranchName, Location, ContactInfo) VALUES (%s, %s, %s)', branches_data)

    # Insert loan type data into LoanTypes table
    cursor.executemany('INSERT INTO LoanTypes (LoanTypeName, Description, InterestRateRange, MaxLoanAmount) VALUES (%s, %s, %s, %s)', loan_types_data)

    conn.commit()
    conn.close()

    print("Sample entries generated successfully.")