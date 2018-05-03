import os
import csv

filepath = os.path.join("pyBank", "budget_data_1.csv")

revenue_data = []

# Read data into dictionary and create a new email field
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        date_name = row["Date"]
        revenue_name = row["Revenue"]




