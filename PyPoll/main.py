import csv
import os

pollData = 'election_data.csv'

voterID = []
county = []
candidate = []
countcandidate = {}

totalVotes = 0
countname = 0
winner = 0

percent_candidate1 = 0
percent_candidate2 = 0
percent_candidate3 = 0
percent_candidate4 = 0
candidate1 = 0
candidate2 = 0
candidate3 = 0
candidate4 = 0

with open(pollData) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        voterID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    totalVotes = len(voterID)
    #print(totalVotes)

    for name in candidate:
        if name in countcandidate:
            countcandidate[name] += 1
        else:
            countcandidate[name] = 1

    candidate1 = countcandidate['Khan']
    candidate2 = countcandidate['Correy']
    candidate3 = countcandidate['Li']
    candidate4 = countcandidate["O'Tooley"]

    if candidate1 > candidate2 and candidate1 > candidate3 and candidate1 > candidate4:
        winner = candidate1
    elif candidate2 > candidate1 and candidate2 > candidate3 and candidate2 > candidate4:
        winner = candidate2
    elif candidate3 > candidate1 and candidate3 > candidate2 and candidate3 > candidate4:
        winner = candidate3
    else:
        winner = candidate4

    if winner == candidate1:
        winner_name = "Khan"
    elif winner == candidate2:
        winner_name = "Correy"
    elif winner == candidate3:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley"


    percent_candidate1 = ('%.4f'%((candidate1/totalVotes) * 100))
    percent_candidate2 = ('%.4f'%((candidate2/totalVotes) * 100))
    percent_candidate3 = ('%.4f'%((candidate3/totalVotes) * 100))
    percent_candidate4 = ('%.4f'%((candidate4/totalVotes) * 100))

    print('Election Results')
    print('-----------------------------')
    print(f'Total Votes: {totalVotes}')
    print('-----------------------------')
    print(f'Khan: {percent_candidate1}% ({candidate1})')
    print(f'Correy: {percent_candidate2}% ({candidate2})')
    print(f'Li: {percent_candidate3}% ({candidate3})')
    print(f"O'Tooley: {percent_candidate4}% ({candidate4})")
    print('-----------------------------')
    print(f'Winner: {winner_name}')
    print('-----------------------------')

output_file = os.path.join("output.txt")

with open(output_file, "w", newline="") as txtfile:
    txtfile.write('Election Results\n')
    txtfile.write('-----------------------------\n')
    txtfile.write(f'Total Votes: {totalVotes}\n')
    txtfile.write('-----------------------------\n')
    txtfile.write(f'Khan: {percent_candidate1}% ({candidate1})\n')
    txtfile.write(f'Correy: {percent_candidate2}% ({candidate2})\n')
    txtfile.write(f'Li: {percent_candidate3}% ({candidate3})\n')
    txtfile.write(f"O'Tooley: {percent_candidate4}% ({candidate4})\n")
    txtfile.write('-----------------------------\n')
    txtfile.write(f'Winner: {winner_name}\n')
    txtfile.write('-----------------------------\n')


