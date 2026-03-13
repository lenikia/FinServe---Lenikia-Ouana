import json
from pathlib import Path


def save_json(data: dict, output_path: str) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def print_extracted_data(data: dict) -> None:
    print("\nLoan Application Data Extracted:\n")
    for key, value in data.items():
        print(f"{key}: {value}")