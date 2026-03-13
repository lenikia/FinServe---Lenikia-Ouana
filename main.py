from app.parser import load_text_file
from app.extractor import extract_loan_application_data
from app.utils import save_json, print_extracted_data


def main():
    input_path = "data/sample_application.txt"
    output_path = "outputs/extracted_application.json"

    text = load_text_file(input_path)
    extracted_data = extract_loan_application_data(text)

    print_extracted_data(extracted_data)
    save_json(extracted_data, output_path)


if __name__ == "__main__":
    main()