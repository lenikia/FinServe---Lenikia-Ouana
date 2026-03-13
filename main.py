from pathlib import Path
from app.extractor import extract_loan_application_data
import json


def main():

    input_file = Path("data/sample_application.txt")

    text = input_file.read_text(encoding="utf-8")

    extracted_data = extract_loan_application_data(text)

    print("Extracted Data:")
    print(extracted_data)

    output_file = Path("outputs/extracted_application.json")
    output_file.parent.mkdir(exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(extracted_data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()