import os
import csv


path = "../Resources/election_data.csv"

total_count = 0
total_votes = 0
khan_count = 0
correy_count = 0
li_count = 0
otooley_count = 0
max_vote_count = 0

def percentage(part, whole):
    return 100 * float(part)/float(whole)
candidate_vote = {}
candidate_name = []
percentage = []
winner = ""

with open(path) as data_file:
    csvreader = csv.reader(data_file)

    for candidate in csvreader:
        candidate_name.append(candidate[2])
        if (candidate[2] == "Khan"):
            khan_count = khan_count + 1
        if (candidate[2] == "Correy"):
            correy_count = correy_count + 1
        if (candidate[2] == "Li"):
            li_count = li_count + 1
        else:
            otooley_count = otooley_count + 1

    winning_value = max(khan_count, li_count, correy_count, otooley_count)
    if (winning_value == khan_count):
        winner = "Khan"
    if (winning_value == li_count):
        winner = "Li"
    if (winning_value == correy_count):
        winner = "Correy"
    else:
        winner = "O'Tooley"

    print("Election Results")
    print("---------------")
    print(f'Total Votes: ', khan_count + li_count + correy_count + otooley_count)
    print('-------------------')
    print("Khan: ", khan_count)
    print("Li: ", li_count)
    print("Correy: ", correy_count)
    print("O'Tooley: ", otooley_count)
    print('-------------------')
    print('Winner: ', winner)