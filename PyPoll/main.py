import csv
import os

totalVotes = 0
cvote = 0

filepath = os.path.join("PyPoll","election_data_1.csv")
with open(filepath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile)
    for row in csvreader:
    #Counts the number of Voters
        totalVotes = sum(1 for _ in csvreader)
    #Dictionary Reader of data set
    dictreader = csv.DictReader(csvfile)
    for lines in dictreader:
        #find popular candidates
        cvote = sum({"Candidates"})
       
 

print("Total Votes:", + totalVotes)
print("Winner:", + (cvote))