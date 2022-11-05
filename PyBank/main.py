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

print(changes)


print('---')
print('Financial Analysis')
print('---------------------------')
print('Total Months: {}'.format(total_months))
print('Total: ${}'.format(net_total))
print('Average Change: ${}'.format(average_change))
print('Greatest Increase in Profits: {} (${})'.format(gi_month, greatest_increase))
print('Greatest Decrease in Profits: {} (${})'.format(gd_month, greatest_decrease))
print('---')

 #```text
 # Financial Analysis
 # ----------------------------
 # Total Months: 86
 # Total: $22564198
 # Average Change: $-8311.11
 # Greatest Increase in Profits: Aug-16 ($1862002)
 # Greatest Decrease in Profits: Feb-14 ($-1825558)
 # ```
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#Consider what you've learned so far. You've learned how to import modules like `csv`; to read and write files in various formats; 
 #to store contents in variables, lists, and dictionaries; to iterate through basic data structures; and to debug along the way. 
 #Using what you've learned, try to break down your tasks into discrete mini-objectives.