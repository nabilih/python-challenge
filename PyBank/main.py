import os
import csv

# Homework 3 - Python Challenge
# PyBank
# Homa Nabili

# input file
SourceFile = os.path.join("Resources", "budget_data.csv")

#Open input data file
with open(SourceFile, newline='') as inputFile:
    csvreader = csv.reader(inputFile, delimiter=',')
    #skip header
    header = next(csvreader)
    
    #####initialize variables#####
    PrevPF = 0
    total = 0   # total net of profit/loss changes
    count  = 0
    CurrentChange = 0.0
    # The total number of months included in the dataset
    totalNum = 0
    # The net total amount of "Profit/Losses" over the entire period
    totalNet = 0 
    # The average of the changes in "Profit/Losses" over the entire period
    AverageChange = 0.0
    # The greatest increase in profits (date and amount) over the entire period
    AverageInc = 0.0
    # The greatest decrease in losses (date and amount) over the entire period
    AverageDec = 0.0
    # The greatest increase in profits (date and amount) over the entire period
    MaxIncrease = 0
    MaxIncreaseDate = ''
    # The greatest decrease in losses (date and amount) over the entire period
    MaxDecrease = 0
    MaxDecreaseDate = ''

    #skip first data row, comparison starts between row 2 of data and row 1
    firstRow  = next(csvreader)
    #store first row's profit/loss data
    PrevPF = int(firstRow[1])
    #start adding up the total
    totalNet = totalNet + int(firstRow[1])

    #loop through the data and calculate the change by comparing current row vs previous row
    for row in csvreader:
        CurrentChange = int(row[1]) - PrevPF 
        PrevPF = int(row[1])
        totalNet += int(row[1])
        total = total + CurrentChange
        count = count +1
        # if change increased in positive direction and is greater than previously stored max amount, 
        # store this new change as the latest maximum increase; also store date
        if CurrentChange >= 0 and CurrentChange > MaxIncrease:
            MaxIncrease = CurrentChange
            MaxIncreaseDate = row[0]
        # if change increased in negative direction and is less than previously stored max amount, 
        # store this new change as the latest maximum decrease; also store date       
        if CurrentChange < 0 and CurrentChange < MaxDecrease:
            MaxDecrease = CurrentChange
            MaxDecreaseDate = row[0]

    AverageChange = round(total/count, 2)

#open output file and save the results
with open('output.txt', 'w') as outputFile:
    outputFile.write('Financial Analysis\n')
    outputFile.write('----------------------------\n')
    outputFile.writelines("Total Months: " + str(count+1) + '\n')
    outputFile.writelines('Total: $' + str(totalNet) + '\n')
    outputFile.writelines('Average Change: $' + str(AverageChange) + '\n')
    outputFile.writelines('Greatest Increase in Profits: ' + str(MaxIncreaseDate) + ' ($' + str(MaxIncrease) + ')\n')
    outputFile.writelines('Greatest Decrease in Profits: ' + str(MaxDecreaseDate) + ' ($' + str(MaxDecrease) + ')\n')
outputFile.close()

print('Financial Analysis')
print('----------------------------')
print("Total Months: " + str(count+1))
print('Total: $' + str(totalNet))
print('Average Change: $' + str(AverageChange))
print('Greatest Increase in Profits: ' + str(MaxIncreaseDate) + ' ($' + str(MaxIncrease) + ')')
print('Greatest Decrease in Profits: ' + str(MaxDecreaseDate) + ' ($' + str(MaxDecrease) + ')')
