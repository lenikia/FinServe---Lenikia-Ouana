import re

def extract_field(pattern: str, text: str):
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None


def extract_loan_application_data(text: str):

    data = {
        "client_name": extract_field(r"Client Name:\s*(.*)", text),
        "company": extract_field(r"Company:\s*(.*)", text),
        "loan_amount": extract_field(r"Loan Amount:\s*(.*)", text),
        "purpose": extract_field(r"Purpose:\s*(.*)", text),
        "repayment_period": extract_field(r"Repayment Period:\s*(.*)", text),
        "email": extract_field(r"Email:\s*(.*)", text),
        "phone": extract_field(r"Phone:\s*(.*)", text),
    }

    return data