import streamlit as st
from app.extractor import extract_loan_application_data

st.set_page_config(page_title="FinServe Loan Application Processor", layout="centered")

st.title("FinServe Loan Application Processor")
st.write("Upload a loan application text file or paste the application text below to extract structured data.")

uploaded_file = st.file_uploader("Upload a .txt loan application", type=["txt"])

text_input = st.text_area("Or paste the loan application text here", height=250)

text_to_process = ""

if uploaded_file is not None:
    text_to_process = uploaded_file.read().decode("utf-8")

elif text_input.strip():
    text_to_process = text_input.strip()

if st.button("Extract Data"):
    if not text_to_process:
        st.warning("Please upload a file or paste some text first.")
    else:
        extracted_data = extract_loan_application_data(text_to_process)

        st.subheader("Extracted Loan Application Data")
        st.json(extracted_data)