
import csv

file_input =  "budget_data.csv"
file_output = "budget_analysis.txt"

total_months = 0
total_revenue = 0
pre_revenue = 0
month_of_change = []
revenue_change_list = []
biggest_decr = ['', 99999999999]
biggest_incr = ['', 0]

with open(file_input,newline="") as csvfile:  
    reader = csv.DictReader(csvfile)
    for row in reader:
        
        total_months += 1
        
        total_revenue += int(row['Profit/Losses'])

       
        rev_change = int(row['Profit/Losses'])- pre_revenue
        pre_revenue = int(row['Profit/Losses'])
        revenue_change_list = revenue_change_list + [rev_change]
        month_of_change = month_of_change + [row['Date']]
        
        if rev_change>biggest_incr[1]:
            biggest_incr[0] = row['Date']
            biggest_incr[1]= rev_change
        
        if rev_change<biggest_decr[1]:
            biggest_decr[0] = row['Date']
            biggest_decr[1]= rev_change

rev_avg = sum(revenue_change_list)/len(revenue_change_list)


print("Average Change in Revenue: $ " + str(rev_avg))
print("Total Months: " + str(total_months))
print("Total Revenue: $ " + str(total_revenue))
print(biggest_incr)
print(biggest_decr)



with open(file_output, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total Revenue: $%d\n" % total_revenue)
    file.write("Average Revenue Change $%d\n" % rev_avg)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (biggest_incr[0], biggest_incr[1]))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (biggest_decr[0], biggest_decr[1]))