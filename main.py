from pathlib import Path
from app.parser import load_text_file
from app.extractor import extract_loan_application_data
from app.utils import save_json, print_extracted_data


def main():
    print("=== FinServe Loan Application Processor ===\n")

    input_path = input("Enter the path of the loan application text file: ").strip()

    if not Path(input_path).exists():
        print("\nError: File not found. Please check the path and try again.")
        return

    text = load_text_file(input_path)
    extracted_data = extract_loan_application_data(text)

    print_extracted_data(extracted_data)

    input_file_name = Path(input_path).stem
    output_path = f"outputs/{input_file_name}_extracted.json"

    save_json(extracted_data, output_path)

    print(f"\nStructured data saved to: {output_path}")


if __name__ == "__main__":
    main()