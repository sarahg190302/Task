import csv
import json

# Load JSON Data
json_data = []
with open('data.json', 'r') as json_file:
    json_data = json.load(json_file)

# Read CSV File
csv_data = []
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        csv_data.append(row)

# Check Availability of CSV Data in JSON
available_ids = set(entry['id'] for entry in json_data)

if any(row['id'] in available_ids for row in csv_data):
    print("JSON data is available.")
else:
    # Create New CSV File with JSON Data and Additional 20 Records
    new_csv_data = csv_data[:20] + json_data

    # Write New CSV File
    with open('new_combined_data.csv', 'w', newline='') as new_csv_file:
        fieldnames = new_csv_data[0].keys()  # Assuming all entries have the same keys
        csv_writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for row in new_csv_data:
            csv_writer.writerow(row)