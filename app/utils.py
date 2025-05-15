import os
import json
import re


def extract_info(text):
    # Basic pattern matching for demo; refine as needed
    name = re.search(r"\b(?:I'm|I am)\s+([A-Za-z]+)", text)
    budget = re.search(r"(\d+\s?(lakh|lakhs|crore))", text, re.IGNORECASE)
    property_type = re.search(r"\b(plot|apartment|flat|villa|land)\b", text, re.IGNORECASE)
    location = re.search(r"in\s+([A-Za-z ]+)", text)

    return {
        "name": name.group(1) if name else None,
        "budget": budget.group(1) if budget else None,
        "property_type": property_type.group(1) if property_type else None,
        "location": location.group(1).strip() if location else None,
        "preferences": text
    }


def main():
    base_path = "data/transcript"
    structured_data = []

    for file in os.listdir(base_path):
        if file.endswith(".txt"):
            with open(os.path.join(base_path, file), "r", encoding="utf-8") as f:
                text = f.read()
                structured_data.append(extract_info(text))

    # Save to JSON
    with open("data/structured_data.json", "w", encoding="utf-8") as out:
        json.dump(structured_data, out, indent=4)


if __name__ == "__main__":
    main()
