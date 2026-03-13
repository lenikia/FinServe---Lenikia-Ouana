import re


def extract_field(pattern: str, text: str):
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None


def extract_email(text: str):
    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    return match.group(0) if match else None


def extract_phone(text: str):
    match = re.search(r'(\+\d{7,15})', text)
    return match.group(1) if match else None


def extract_loan_amount(text: str):
    patterns = [
        r"Loan Amount:\s*(.*)",
        r"request a loan of\s*([0-9.,]+\s*[A-Z]{3})",
        r"loan of\s*([0-9.,]+\s*[A-Z]{3})"
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return None


def extract_client_name(text: str):
    patterns = [
        r"Client Name:\s*(.*)",
        r"My name is\s*([A-Z][a-zA-Z]+\s+[A-Z][a-zA-Z]+)"
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return None


def extract_company(text: str):
    patterns = [
        r"Company:\s*(.*)",
        r"on behalf of\s*([A-Z][A-Za-z0-9& ]+)"
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip().rstrip(".")
    return None


def extract_purpose(text: str):
    patterns = [
        r"Purpose:\s*(.*)",
        r"for\s*([a-zA-Z ]+)"
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            value = match.group(1).strip().rstrip(".")
            if len(value) < 60:
                return value
    return None


def extract_repayment_period(text: str):
    patterns = [
        r"Repayment Period:\s*(.*)",
        r"repayment period of\s*(.*)",
        r"over\s*(\d+\s*months?)"
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return None


def extract_loan_application_data(text: str):
    data = {
        "client_name": extract_client_name(text),
        "company": extract_company(text),
        "loan_amount": extract_loan_amount(text),
        "purpose": extract_purpose(text),
        "repayment_period": extract_repayment_period(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
    }

    return data