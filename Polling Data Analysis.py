import os
import csv

filepath = os.path.join("Resources","election_data.csv")

with open(filepath,"r",newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")

    header = next(csvreader)

    election = {}

    total_votes = 0

    for row in csvreader:
        if row[2] not in election.keys():
            election[row[2]] = 1
        else:
            election[row[2]] += 1
        total_votes += 1

winner_vote = 0
print(" ")
print(" ")
print("Election Results")
print("------------------------------------------")

for key,value in election.items():
    print(f"{key} : {round(value/total_votes*100,3)}% ({value})")
    if election[key]> winner_vote:
        winner = key
        winner_vote = election[key]

print("--------------------------------------------")
print(f"Winner: {winner}")
print("--------------------------------------------")

    



