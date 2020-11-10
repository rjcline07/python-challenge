
# bringing in necessities for csv module
import os
import csv

#opening and reading proper csv, establishing output file as well
data_csv = os.path.join("Resources","election_data.csv")
analysis_txt = os.path.join("Analysis","election_analysis.txt")

# Total Vote Count and Candidate Options
total_votes = 0
candidates = []
candidate_votes = {}

#Reading in CSV

with open(data_csv) as election_data:
    reader = csv.reader(election_data)


    #Header
    header = next(reader)

    #setting up for loop
    for row in reader:
        print(". ", end = ""),
        total_votes += 1
        #pulling candidate name
        candidate_name = row[2]

#making sure new candidates are added to list
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        #adding vote to candidate count
        candidate_votes[candidate_name] += 1

