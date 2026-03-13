# FinServe Loan Application Processor

This project presents a proof-of-concept solution designed to automate the extraction of key information from loan application texts.

The goal is to demonstrate how FinServe could reduce manual data entry by automatically converting unstructured or semi-structured loan requests (such as emails or text submissions) into structured data ready for internal systems.

## Features

- Upload a loan application text file (.txt)
- Paste loan application text directly
- Automatic extraction of key fields:
  - Client Name
  - Company
  - Loan Amount
  - Purpose
  - Repayment Period
  - Email
  - Phone
- Structured output in JSON format

## Technologies Used

- Python
- Regular Expressions (Regex)
- Streamlit for the user interface

## How to Run the Project

1. Clone the repository

2. Install dependencies

pip install -r requirements.txt

3. Run the application

streamlit run streamlit_app.py

4. Open in browser
