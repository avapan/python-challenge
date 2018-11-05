#In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses.
#  (Thankfully, your company has rather lax standards for accounting so the records are simple.)

#total number of months included in the dataset
#The average change in "Profit/Losses" between months over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
import csv
import os

file_path =("budget-data.csv")

months = []
profit_losses = []

with open(file_path, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    
    next(csvread, None)

    for row in csvread:
        months.append(row[0])
        profit_losses.append(int(row[1]))

total_months = len(months)

greatest_inc = profit_losses[0]
greatest_dec = profit_losses[0]
total_profit_losses = 0

for r in range(len(profit-losses)):
    if profit_losses[r] >= greatest_inc:
        greatest_inc = profit_losses[r]
        greatest_inc_month = months[r]
    elif profit_losses[r] <= greatest_dec:
        greatest_dec = profit_losses[r]
        greatest_dec_month = months[r]
    total_profit_losses += profit_losses[r]

average_change = round(total_profit_losses/total_months, 2)

output_path = os.path.join('PyBank','pybank_output' + '.txt')

with open(output_path, 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Total Profit_Losses: $' + str(total_profit_losses) + '\n')
    writefile.writelines('Average Revenue Change: $' + str(average_change) + '\n')
    writefile.writelines('Greatest Increase in Revenue: ' + greatest_inc_month + ' ($' + str(greatest_inc) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Revenue: ' + greatest_dec_month + ' ($' + str(greatest_dec) + ')')

with open(output_path, 'r') as readfile:
    print(readfile.read())