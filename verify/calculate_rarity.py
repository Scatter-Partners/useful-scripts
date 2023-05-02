import json
import os
import csv
from collections import defaultdict

folder_name = "json"

# Create a dictionary to keep track of trait counts
traits = defaultdict(lambda: defaultdict(int))
traits_original = defaultdict(lambda: defaultdict(int))

# Loop through all the files in the "JSON" folder
for filename in os.listdir(folder_name):
    # # Ignore non-JSON files
    # if not filename.endswith(".json"):
        # continue
    # Load the JSON file
    with open(os.path.join(folder_name, filename)) as f:
        data = json.load(f)
    # Count the traits in the attributes field
    for attribute in data["attributes"]:
        trait_type = attribute["trait_type"]
        # trait_type = trait_type.replace("Example ", "")
        value = attribute["value"]
        traits[trait_type][value] += 1
        traits_original[trait_type][value] += 1


# Calculate the total count for each trait_type
trait_counts = {trait_type: sum(trait_values.values()) for trait_type, trait_values in traits.items()}
#print(trait_counts)

# Calculate the rarity percentage for each trait value
for trait_type, trait_values in traits.items():
    #print(trait_values.items())
    for value, count in trait_values.items():
        rarity_percentage = count / trait_counts[trait_type] * 100
        rarity_percentage = round(rarity_percentage, 2)
        traits[trait_type][value] = rarity_percentage

# Write the results to a CSV file
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Trait Type", "Value", "Count", "Rarity Percentage"])
    for trait_type, trait_values in traits.items():
        for value, rarity_percentage in trait_values.items():
            count = traits_original[trait_type][value] #traits[trait_type][value] * trait_counts[trait_type] / 100
            writer.writerow([trait_type, value, count, rarity_percentage])
