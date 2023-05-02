import os
import json
import csv

# Set the folder path containing JSON files
json_folder = "json"

# Create a list of JSON file paths
json_files = [os.path.join(json_folder, file) for file in os.listdir(json_folder) if file.endswith('.json')]

# Initialize the CSV data
csv_data = []

# Loop through the JSON files
for json_file in json_files:
    with open(json_file, 'r') as file:
        data = json.load(file)

        # Extract name, description, and image fields
        row = {
            'name': data['name'],
            'description': data['description'],
            'image': data['image']
        }

        # Loop through attributes
        for attribute in data['attributes']:
            trait_type = attribute['trait_type']
            value = attribute['value']

            # Add the trait_type and value to the row
            row[trait_type] = value

        # Add the row to the CSV data
        csv_data.append(row)

# Get unique column names from the csv_data
csv_columns = set()
for row in csv_data:
    csv_columns.update(row.keys())

# Write the CSV data to the output.csv file
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for row in csv_data:
        writer.writerow(row)
