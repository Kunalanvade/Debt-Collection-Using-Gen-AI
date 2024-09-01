import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random

# Initialize Faker
fake = Faker()

# Function to generate random payment history
def generate_payment_history():
    return np.random.choice(
        [
            "On-time",
            "Late payments in last month",
            "Late payments in last 3 months",
            "Late payments in last 6 months",
            "Missed last payment",
            "Missed 2 payments",
            "Missed last 3 payments",
        ]
    )

# Function to generate random financial status
def generate_financial_status():
    return np.random.choice(["Good", "Moderate", "Poor"])

# Function to generate random income
def generate_income():
    return round(np.random.uniform(20000, 120000), 2)

# Function to generate a random loan tenure in months
def generate_tenure_in_months():
    return np.random.randint(6, 51)  # Loan tenure between 6 months and 50 months

# Function to generate random communication status
def generate_communication_status():
    return np.random.choice(["Contacted", "Not Contacted", "In Progress"])

# Function to generate random communication preference
def generate_communication_preference():
    return np.random.choice(["Email", "SMS", "Letter"])

# Function to generate a random Indian phone number
def generate_phone_number():
    return f"+91{random.randint(7000000000, 9999999999)}"  # Indian phone numbers

# Function to generate a random current balance
def generate_current_balance():
    return round(np.random.uniform(40000, 60000), 2)

# Function to format dates to yyyy-mm-dd
def format_date(date):
    return date.strftime("%Y-%m-%d")

# Create a list to store the data
data = []

# Specific borrowers
specific_borrowers = [
    {
        "Borrower_ID": 1,
        "Borrowers_Name": "Kunal Anvade",
        "Loan_Amount": round(np.random.uniform(10000, 1000000), 2),
        "Outstanding_Balance": round(np.random.uniform(100, 5000), 2),
        "Due_Date": format_date(fake.date_between(start_date="today", end_date="+90d")),
        "Payment_History": generate_payment_history(),
        "Communication_Preference": generate_communication_preference(),
        "Financial_Status": generate_financial_status(),
        "Last_Payment_Date": format_date(fake.date_between(start_date="-1y", end_date="today")),
        "Last_Payment_Amount": round(np.random.uniform(0, 5000), 2),
        "Email": "kunalanvade20@gmail.com",
        "Phone": "9371452689",
        "Income": generate_income(),
        "Tenure_In_Months": generate_tenure_in_months(),
        "Communication_Status": generate_communication_status(),
        "Current_Balance": generate_current_balance()
    },
    {
        "Borrower_ID": 2,
        "Borrowers_Name": "Vaishnavi Patil",
        "Loan_Amount": round(np.random.uniform(10000, 1000000), 2),
        "Outstanding_Balance": round(np.random.uniform(100, 5000), 2),
        "Due_Date": format_date(fake.date_between(start_date="today", end_date="+90d")),
        "Payment_History": generate_payment_history(),
        "Communication_Preference": generate_communication_preference(),
        "Financial_Status": generate_financial_status(),
        "Last_Payment_Date": format_date(fake.date_between(start_date="-1y", end_date="today")),
        "Last_Payment_Amount": round(np.random.uniform(0, 5000), 2),
        "Email": "vishupatil8571@gmail.com",
        "Phone": "8080323464",
        "Income": generate_income(),
        "Tenure_In_Months": generate_tenure_in_months(),
        "Communication_Status": generate_communication_status(),
        "Current_Balance": generate_current_balance()
    },
    {
        "Borrower_ID": 3,
        "Borrowers_Name": "Tejashri Tisage",
        "Loan_Amount": round(np.random.uniform(10000, 1000000), 2),
        "Outstanding_Balance": round(np.random.uniform(100, 5000), 2),
        "Due_Date": format_date(fake.date_between(start_date="today", end_date="+90d")),
        "Payment_History": generate_payment_history(),
        "Communication_Preference": generate_communication_preference(),
        "Financial_Status": generate_financial_status(),
        "Last_Payment_Date": format_date(fake.date_between(start_date="-1y", end_date="today")),
        "Last_Payment_Amount": round(np.random.uniform(0, 5000), 2),
        "Email": "tejashri1404@gmail.com",
        "Phone": "8483850934",
        "Income": generate_income(),
        "Tenure_In_Months": generate_tenure_in_months(),
        "Communication_Status": generate_communication_status(),
        "Current_Balance": generate_current_balance()
    },
    {
        "Borrower_ID": 4,
        "Borrowers_Name": "Sachin Chaughule",
        "Loan_Amount": round(np.random.uniform(10000, 1000000), 2),
        "Outstanding_Balance": round(np.random.uniform(100, 5000), 2),
        "Due_Date": format_date(fake.date_between(start_date="today", end_date="+90d")),
        "Payment_History": generate_payment_history(),
        "Communication_Preference": generate_communication_preference(),
        "Financial_Status": generate_financial_status(),
        "Last_Payment_Date": format_date(fake.date_between(start_date="-1y", end_date="today")),
        "Last_Payment_Amount": round(np.random.uniform(0, 5000), 2),
        "Email": "sachinchougule5762@gmail.com",
        "Phone": "9325295762",
        "Income": generate_income(),
        "Tenure_In_Months": generate_tenure_in_months(),
        "Communication_Status": generate_communication_status(),
        "Current_Balance": generate_current_balance()
    },
    {
        "Borrower_ID": 5,
        "Borrowers_Name": "Aastha Bhagat",
        "Loan_Amount": round(np.random.uniform(10000, 1000000), 2),
        "Outstanding_Balance": round(np.random.uniform(100, 5000), 2),
        "Due_Date": format_date(fake.date_between(start_date="today", end_date="+90d")),
        "Payment_History": generate_payment_history(),
        "Communication_Preference": generate_communication_preference(),
        "Financial_Status": generate_financial_status(),
        "Last_Payment_Date": format_date(fake.date_between(start_date="-1y", end_date="today")),
        "Last_Payment_Amount": round(np.random.uniform(0, 5000), 2),
        "Email": "aasthabhagat17@gmail.com",
        "Phone": "9049649099",
        "Income": generate_income(),
        "Tenure_In_Months": generate_tenure_in_months(),
        "Communication_Status": generate_communication_status(),
        "Current_Balance": generate_current_balance()
    },
    {
        "Borrower_ID": 6,
        "Borrowers_Name": "Atharva Varade",
        "Loan_Amount": round(np.random.uniform(10000, 1000000), 2),
        "Outstanding_Balance": round(np.random.uniform(100, 5000), 2),
        "Due_Date": format_date(fake.date_between(start_date="today", end_date="+90d")),
        "Payment_History": generate_payment_history(),
        "Communication_Preference": generate_communication_preference(),
        "Financial_Status": generate_financial_status(),
        "Last_Payment_Date": format_date(fake.date_between(start_date="-1y", end_date="today")),
        "Last_Payment_Amount": round(np.random.uniform(0, 5000), 2),
        "Email": "atharvavarade1@gmail.com",
        "Phone": "9309499549",
        "Income": generate_income(),
        "Tenure_In_Months": generate_tenure_in_months(),
        "Communication_Status": generate_communication_status(),
        "Current_Balance": generate_current_balance()
    }
]

# Add specific borrowers to the data list
for borrower in specific_borrowers:
    data.append([
        borrower["Borrower_ID"],
        borrower["Borrowers_Name"],
        borrower["Loan_Amount"],
        borrower["Outstanding_Balance"],
        borrower["Due_Date"],
        borrower["Payment_History"],
        borrower["Communication_Preference"],
        borrower["Financial_Status"],
        borrower["Last_Payment_Date"],
        borrower["Last_Payment_Amount"],
        borrower["Email"],
        borrower["Phone"],
        borrower["Income"],
        borrower["Tenure_In_Months"],
        borrower["Communication_Status"],
        borrower["Current_Balance"]
    ])

# Generate the remaining data
for i in range(len(specific_borrowers), 100):
    data.append([
        i + 1,
        fake.name(),
        round(np.random.uniform(10000, 1000000), 2),
        round(np.random.uniform(100, 5000), 2),
        format_date(fake.date_between(start_date="today", end_date="+90d")),
        generate_payment_history(),
        generate_communication_preference(),
        generate_financial_status(),
        format_date(fake.date_between(start_date="-1y", end_date="today")),
        round(np.random.uniform(0, 5000), 2),
        fake.email(),
        generate_phone_number(),
        generate_income(),
        generate_tenure_in_months(),
        generate_communication_status(),
        generate_current_balance()
    ])

# Create DataFrame
df = pd.DataFrame(
    data,
    columns=[
        "Borrower_ID",
        "Borrowers_Name",
        "Loan_Amount",
        "Outstanding_Balance",
        "Due_Date",
        "Payment_History",
        "Communication_Preference",
        "Financial_Status",
        "Last_Payment_Date",
        "Last_Payment_Amount",
        "Email",
        "Phone",
        "Income",
        "Tenure_In_Months",
        "Communication_Status",
        "Current_Balance"
    ]
)

# Save to CSV
df.to_csv("borrowers_data.csv", index=False)