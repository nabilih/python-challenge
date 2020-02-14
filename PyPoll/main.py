import os
import csv

# Homework 3 - Python Challenge
# PyPoll
# Homa Nabili

# input file
SourceFile = os.path.join("Resources", "election_data.csv")

TotalVotes = 0
candidates = []
CandidateVotes = {}

with open(SourceFile, newline='') as inputFile:
    csvreader = csv.reader(inputFile, delimiter=',')
    #skip header
    header = next(csvreader)

    for row in csvreader:
        TotalVotes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
        if row[2] in CandidateVotes:
            CandidateVotes[row[2]] += 1
        else:
            CandidateVotes[row[2]] = 1

percent = 0.0

#open output file and save the results
with open('VotingResult.txt', 'w') as outputFile:
    outputFile.write('Election Results\n')
    outputFile.write('----------------------------\n')
    outputFile.writelines("Total Votes: " + str(TotalVotes) + '\n')
    outputFile.write('----------------------------\n')

    print('Election Results')
    print('----------------------------')
    print("Total Votes: " + str(TotalVotes))
    print('----------------------------')

    for item in CandidateVotes:
        Percent = round((CandidateVotes[item] / TotalVotes) * 100, 3)
        outputFile.write(item + ': ' + str(Percent) + '% (' + str(CandidateVotes[item]) + ')\n')
        print(item + ': ' + str(Percent) + '% (' + str(CandidateVotes[item]) + ')')

    outputFile.write('----------------------------\n')
    print('----------------------------')
    winner = max(CandidateVotes, key=CandidateVotes.get)
    outputFile.write('Winner: ' + winner + '\n')
    outputFile.write('----------------------------\n')
    print('Winner: ' + winner)
    print('----------------------------')
outputFile.close()
