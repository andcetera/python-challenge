import os
import csv

#path to the report
csvpath = os.path.join('Resources', 'budget_data.csv')

# The total number of months included in the dataset
total_months = 0
# The net total amount of "Profit/Losses" over the entire period
net_total = 0
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
average_change = 0.0  # hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
# The greatest increase in profits over the entire period
greatest_increase = 0
# The greatest decrease in profits over the entire period
greatest_decrease = 0

#open the csv report
with open(csvpath, 'r') as csvfile:

        #open a csv reader
        csvreader = csv.reader(csvfile, delimiter=',')

        #store the header in a variable for later
        header = next(csvreader)

        #iterate through each row in the report
        for row in csvreader:

            #count the total months in the report
            total_months += 1

            #create a variable to cast the profit/loss column value to an integer for simplicity
            r = int(row[1])
            
            #add the profit/loss to a running total
            net_total += r

            #check profit/loss against greatest increase/decrease and update date & amount as found
            if r > greatest_increase:
                greatest_increase = r
                gi_month = row[0]
            
            if r < greatest_decrease:
                greatest_decrease = r
                gd_month = row[0]



print(total_months, net_total, gi_month, greatest_increase, gd_month, greatest_decrease)











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