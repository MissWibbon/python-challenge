import os
import csv

path = os.path.join(".", "Resources", "budget_data.csv")
total_m = 0
with open(path) as data_file:
    data_csv = csv.reader(data_file)
    header = next(data_csv)

    for row in data_csv:
        total_m +=1
print("Total Month", total_m)