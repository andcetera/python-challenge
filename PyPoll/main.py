import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
# The total number of votes cast
total_votes = 0
# A complete list of candidates who received votes
candidates = []
# The percentage of votes each candidate won
percentages = {}
# The total number of votes each candidate won
count_won = {}
# The winner of the election based on popular vote.

#open the csv report
with open(csvpath, 'r') as csvfile:

        #open a csv reader
        csvreader = csv.reader(csvfile, delimiter=',')

        #store the header in a variable for later
        header = next(csvreader)

        #iterate through each row in the report
        for row in csvreader:

            #running count of total votes
            total_votes += 1

            #check if candidate voted for is included in our list yet, if not, add
            if row[2] not in candidates:
                candidates.append(row[2])

                #initialize candidate vote count
                count_won[candidates[len(candidates)-1]] = 0
            
            #add each vote to each candidate's total
            count_won[row[2]] += 1

        #percentages = {k:(v/total_votes) for (k, v) in count_won}





            

print(total_votes, candidates, count_won, percentages)


 # ```text
 # Election Results
 # -------------------------
 # Total Votes: 369711
 # -------------------------
 # Charles Casper Stockham: 23.049% (85213)
 # Diana DeGette: 73.812% (272892)
 # Raymon Anthony Doane: 3.139% (11606)
 # -------------------------
 # Winner: Diana DeGette
 # -------------------------
 # ```

 #In addition, your final script should both print the analysis to the terminal and export a text file with the results.

 #Consider what you've learned so far. You've learned how to import modules like `csv`; to read and write files in various formats; 
 #to store contents in variables, lists, and dictionaries; to iterate through basic data structures; and to debug along the way. 
 #Using what you've learned, try to break down your tasks into discrete mini-objectives.