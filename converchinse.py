import json
import re

# Load JSON file
with open('chinese_terms.json', 'r', encoding='utf-8') as f:
    data = json.load(f)  # Properly read and parse JSON

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
            "hints": attributes_list,  # Renamed "attributes" to "hints"
            "definition": entry["definition"]
        }
        formatted_data.append(formatted_entry)
    
    return formatted_data

# Apply transformation
formatted_json = reformat_json(data)

# Convert to JSON string and save to file
output_json = json.dumps(formatted_json, ensure_ascii=False, indent=4)

# Save to a new JSON file
with open('formatted_chinese_terms.json', 'w', encoding='utf-8') as f:
    f.write(output_json)

# Print formatted JSON
print(output_json)
