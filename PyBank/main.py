import os
import csv

path = "../Resources/budget_data.csv"
total_month = 0
total_profit = 0
total_loss = 0
Daily_Change = []

Previous_Profit_Loss = 0
with open(path) as data_file:
    data_csv = csv.reader(data_file)

    header = next(data_csv)
    
    for row in data_csv:
        total_month +=1
        profit = int(row[1])
        total_profit = total_profit + profit
        Daily_Change.append(int(row[1]) - Previous_Profit_Loss)
        Previous_Profit_loss = int(row[1])
print("Total Month", total_month)
print(f"Total Profit: ", total_profit)
print(f"Average Change: ", round(float(sum(Daily_Change)/len(Daily_Change)))*100)
