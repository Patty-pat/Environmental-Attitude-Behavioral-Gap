import json

with open('facilities.json', 'w') as json_file:
    json.dump(facilities, json_file, indent=4)

print("Data saved to facilities.json")

import csv

with open('facilities.csv', 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["name", "type", "ownership", "area", "latitude", "longitude"])
    writer.writeheader()
    writer.writerows(facilities)

print("Data saved to facilities.csv")
