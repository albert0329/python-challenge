import csv

budgetPath = 'budget_data.csv'
totalCalc = 0

with open(budgetPath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #remove header line
    csv_header = next(csvreader)

    # calculate total months
    totalMonths = len(csvfile.readlines())

    for row in csvreader:
        totalCalc += int(row[1])
    print(totalCalc)












