import json
import re

# File paths (Update if needed)
input_file = "chinese_terms.json"
output_file = "formatted_chinese_terms.json"

# Load JSON file
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Function to parse term and attributes
def reformat_json(data):
    formatted_data = []
    
    for entry in data:
        match = re.match(r"(.+?)\s*\((.+?)\)", entry["term"])
        if match:
            term, attributes = match.groups()
            attributes_list = [attr.strip() for attr in attributes.split(",")]
        else:
            term = entry["term"]
            attributes_list = []

        formatted_entry = {
            "term": term,
            "hints": attributes_list,
            "definition": entry["definition"]
        }
        formatted_data.append(formatted_entry)
    
    return formatted_data

# Apply transformation
formatted_json = reformat_json(data)

# Convert to JSON string and save to file
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(formatted_json, f, ensure_ascii=False, indent=4)

# Print confirmation message
print(f"Formatted JSON saved to {output_file}")
