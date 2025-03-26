import csv
import json

# Read the CSV file and process data
csv_file =  r"C:\Users\91966\Downloads\Book1.csv" # Change this to your actual file name
json_file = "output.json"

data = []

with open(csv_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        total_price = float(row["Total"])
        item_price = total_price / 2  # Half of the total
        
        # Construct the JSON structure
        entry = {
            "ID": row["ID"],
            "First Name": row["First Name"],
            "Last Name": row["Last Name"],
            "Age": row["Age"],
            "Gender": row["Gender"],
            "Email": row["Email"],
            "Phone Number": row["Phone Number"],
            "Address": row["Address"],
            "City": row["City"],
            "Country": row["Country"],
            "Items": [
                {"Item": "Product 1", "Price": item_price},
                {"Item": "Product 2", "Price": item_price}
            ]
        }
        
        data.append(entry)

# Write to JSON file
with open(json_file, mode='w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)

print(f"CSV converted to JSON successfully! Output file: {json_file}")