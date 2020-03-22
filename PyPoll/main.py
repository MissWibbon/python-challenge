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

with open(path) as data_file:
    csvreader = csv.reader(path, delimiter=',')

    candidate_vote = {}
    candidate_name = []

    for row in csvreader:
        candidate = row[2]

        if candidate not in candidate_name:
            candidate_name.append(candidate)
            candidate_vote[candidate]=1
        
        candidate_vote[candidate]=candidate_vote[candidate]+1

    total_votes = sum(candidate_vote.value())
    percentage = []
    print("Election Results")
    print("---------------")

    output=(
        f'\nElection Results\n'
        f'\------------------')
    print(f'Total Votes: {total_votes}')
    print('-------------------')
    for candidate in candidate_vote:
        percentage=((candidate_vote[candidate]/total_votes)*100)
        print(f'{candidate}: {percentage: 2f}% ({candidate_vote[candidate]}) ')
        output += f'{candidate}'
    for winner in candidate_vote.keys():
        if candidate_vote[winner]==max(candidate_vote.values()):
            candidate_win = winner

        print('--------------------')
        print(f'Winner: {candidate_win}')

        output += (f'Winner: {candidate_win}')
        text_path = os.path.join("election_data.txt")
        with open(text_path,"w") as txtfile:
            txtfile.write(output)