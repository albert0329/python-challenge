import csv

budgetPath = 'budget_data.csv'

date = []
amount = []
avgChange = []

totalMonths = 0
totalAmount = 0
totalAverage = 0



with open(budgetPath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #remove header
    csv_header = next(csvreader)

    for row in csvreader:
        date.append(row[0])
        amount.append(int(row[1]))

    totalMonths = len(date)

    totalAmount = sum(amount)

    for i in range(1, len(amount)):
        #averageChange = amount[i+1] - amount[i]
        avgChange.append(amount[i] - amount[i-1])
    totalAverage = '{0:.2f}'.format(sum(avgChange)/len(avgChange))


















