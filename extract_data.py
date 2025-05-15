import os
import json
import re
import pandas as pd

transcript_dir = "data/transcripts"
structured_data = []

def extract_info(text):
    name = re.search(r"(?:I am|This is|My name is)\s+([A-Z][a-z]+)", text)
    budget = re.search(r"(\d{1,3}\s?(?:lakhs|lakh|Lakhs|Lakhs))", text)
    property_type = re.search(r"(plot|villa|apartment|house|flat)", text, re.IGNORECASE)
    location = re.search(r"in\s+([A-Z][a-z]+)", text)
    preference = re.search(r"(near beach|near hospital|main road|corner plot)", text, re.IGNORECASE)

    return {
        "name": name.group(1) if name else "",
        "budget": budget.group(1) if budget else "",
        "property_type": property_type.group(1).lower() if property_type else "",
        "location": location.group(1) if location else "",
        "preferences": preference.group(1).lower() if preference else ""
    }

for filename in os.listdir(transcript_dir):
    if filename.endswith(".txt"):
        with open(os.path.join(transcript_dir, filename), "r", encoding="utf-8") as file:
            content = file.read()
            data = extract_info(content)
            structured_data.append(data)

# Save to JSON
with open("data/structured_data.json", "w") as f:
    json.dump(structured_data, f, indent=4)

# Optionally, save to Excel
df = pd.DataFrame(structured_data)
df.to_excel("data/structured_data.xlsx", index=False)


print("done the process")
