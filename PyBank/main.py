import csv
import os

budgetPath = 'budget_data.csv'

date = []
amount = []
avgChange = []

totalMonths = 0
totalAmount = 0
totalAverage = 0
greatestInc = 0
greatestDec = 0
avgChange.append(0)



with open(budgetPath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #remove header
    csv_header = next(csvreader)

    for row in csvreader:
        date.append(row[0])
        amount.append(int(row[1]))

    totalMonths = len(date)

    totalAmount = sum(amount)

    #for i in range(1, len(amount)):
        #avgChange.append(amount[i] - amount[i-1])

    for i, x in enumerate(date[:-1],1):
        avgChange.append(int(amount[i])-int(amount[i-1]))

    totalAverage = '{0:.2f}'.format(sum(avgChange)/(len(avgChange)-1))


    greatestInc = max(avgChange)
    greatestIncDate = avgChange.index(greatestInc)

    greatestDec = min(avgChange)
    greatestDecDate = avgChange.index(greatestDec)

    print(f'Total Months: {totalMonths}')
    print(f'Total: ${totalAmount}')
    print(f'Average Change: ${totalAverage}')
    print(f'Greatest Increase in Profits: {date[greatestIncDate]} ({greatestInc})')
    print(f'Greatest Decrease in Profits: {date[greatestDecDate]} ({greatestDec})')

output_file = os.path.join("output.txt")

with open(output_file, "w", newline="") as txtfile:
    txtfile.write(f'Total Months: {totalMonths}\n')
    txtfile.write(f'Total: ${totalAmount}\n')
    txtfile.write(f'Average Change: ${totalAverage}\n')
    txtfile.write(f'Greatest Increase in Profits: {date[greatestIncDate]} ({greatestInc})\n')
    txtfile.write(f'Greatest Decrease in Profits: {date[greatestDecDate]} ({greatestDec})\n')















