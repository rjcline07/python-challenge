
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


#establish a winning candidate and count variable
winning_candidate = ""
winning_count = 0


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

#printing results and exporting

with open(analysis_txt, "w") as txt_file:

    election_results = (
        f"\n\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes}\n"
        f"------------------------\n")
    print(election_results, end="")
#saving final count to txt file
    txt_file.write(election_results)


#finding winner
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
    

    #printing candidate's count and percentage
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

    #txt file of results
        txt_file.write(voter_output)

    #printing winner
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"------------------------\n")
    print(winning_candidate_summary)

    #saving file
    txt_file.write(winning_candidate_summary)
