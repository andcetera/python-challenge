import os
import csv

#path to the report
csvpath = os.path.join('Resources', 'budget_data.csv')

# The total number of months included in the dataset
total_months = 0
# The net total amount of "Profit/Losses" over the entire period
net_total = 0
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
last_month = 0
changes = []
total_ch = 0.0
average_change = 0.0
# The greatest increase in profits over the entire period
greatest_increase = 0
# The greatest decrease in profits over the entire period
greatest_decrease = 0

#open the csv report
with open(csvpath, 'r') as csvfile:

    #open a csv reader
    csvreader = csv.reader(csvfile, delimiter=',')

    #store the report header
    header = next(csvreader)

    #iterate through each row in the report
    for row in csvreader:

        #count the total months in the report
        total_months += 1

        #create a variable to cast the profit/loss column value to an integer for simplicity
        r = int(row[1])
        
        #add the P/L to a running total
        net_total += r

        #keep a running list of changes in month over month P/L
        if last_month !=0:
            changes.append(r-last_month)
            #create a variable to store the latest member of this list for simplicity
            c = changes[len(changes)-1]
        
            #check P/L against greatest increase/decrease and update date & amount as found
            if c > greatest_increase:
                greatest_increase = c
                gi_month = row[0]
                
            if c < greatest_decrease:
                greatest_decrease = c
                gd_month = row[0]

        #update last month's info to compare P/L
        last_month = r

    #get the average of the monthly changes in P/L
    for ch in changes:
        total_ch += ch   
    average_change = round(total_ch/(total_months-1), 2)



print('---')
print('Financial Analysis')
print('---------------------------')
print('Total Months: {}'.format(total_months))
print('Total: ${}'.format(net_total))
print('Average Change: ${}'.format(average_change))
print('Greatest Increase in Profits: {} (${})'.format(gi_month, greatest_increase))
print('Greatest Decrease in Profits: {} (${})'.format(gd_month, greatest_decrease))
print('---')

#path to create finished report
txtpath = os.path.join('Analysis','Financial Report.txt')

#open new file to print finished report
with open(txtpath, 'w') as textfile:
    textfile.write('---\n')
    textfile.write('Financial Analysis\n')
    textfile.write('---------------------------\n')
    textfile.write('Total Months: {}\n'.format(total_months))
    textfile.write('Total: ${}\n'.format(net_total))
    textfile.write('Average Change: ${}\n'.format(average_change))
    textfile.write('Greatest Increase in Profits: {} (${})\n'.format(gi_month, greatest_increase))
    textfile.write('Greatest Decrease in Profits: {} (${})\n'.format(gd_month, greatest_decrease))
    textfile.write('---')


