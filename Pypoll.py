# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize the total vote counter to 0
total_votes=0

#Candidate Options
candidate_options=[]

#Declare the empty dictionary
candidate_votes={}

#WINNING CANDIDATE AND WINNING COUNT TRACKER
winning_candidate=""
winning_count=0
winning_percentage=0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    file_reader=csv.reader(election_data)
    #Read the header row.
    headers=next(file_reader)
   

    #Print each row in the CSV file
    for row in file_reader:
        #Add to the total vote count.
        total_votes=total_votes+1
        
        #Print the candidates name from each row
        candidate_name=row[2]
        
        #If the candidate's name does not match any existing candidate:
        if candidate_name not in candidate_options:
            #Add it to the list of candidates
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name]=0

            #Add a vote to that particular candidate's name
        candidate_votes[candidate_name]+=1
#print(candidate_votes)

#Calculating the percentage of the vote for each candidate by looping through the counts
#Iterate through the candidate list
for candidate_name in candidate_votes:
    #Retrieve vote count of candidate
    votes=candidate_votes[candidate_name]
    #Calculate the percentage of votes for each candidate
    vote_percentage=float(votes)/float(total_votes)*100
    #Print the candidate name and the percentage of votes
    print(f"{candidate_name}: received {vote_percentage:.1f}% of the popular vote!")

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #Determine the winning count and the winning candidate


    #Determine if the votes is greater than the winning count.
    if(votes>winning_count) and (vote_percentage>winning_percentage):
        #If true then set winning_count = votes and winning_percentage = vote_percentage.
        winning_count=votes
        winning_percentage=vote_percentage    
        #And, set the winning_candidate equal to the candidate's name.
        winning_candidate=candidate_name

#Print out the winning candidate, vote count, and percentage to the terminal.

winning_candidate_summary=(
    f'--------------------------------------\n'
    f'Winner:  {winning_candidate}\n'
    f'Winning Vote Count: {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.1f}%\n'
    f'--------------------------------------\n')
print(winning_candidate_summary)





   
                        
        #Add the candidate name to the candidate list.
        #candidate_options.append(candidate_name)
    
    
    
