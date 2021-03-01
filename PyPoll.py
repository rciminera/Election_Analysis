# Data to be retrieved:
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

# Add our dependencies
import csv
import os

# Input and output files
# Assign a variable for the file to load a file from a path
file_to_load = os.path.join("Resources", '/Users/jrobertciminera/Mod3/Election_Analysis/Resources/election_results.csv')
# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", '/Users/jrobertciminera/Mod3/Election_Analysis/Analysis/election_analysis.txt')

# Establish lists, dictionariies, and intitialize counters
# Initialize a total vote counter
total_votes = 0
# Candidate options list and candidate vote dictionary
candidate_options = []
candidate_votes ={}
# Track the winning candidate, vote count, abd percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Read the input file, Count the Votes by Candidate 
# Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with the csv reader Function and store the election_data in file_reader
    file_reader = csv.reader(election_data)
    # Read the header row
    headers = next(file_reader)
    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        # Get the candidate name from each row
        candidate_name = row[2]
        # If the candidate name does not match any existing candidate add to the candidate list
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#Print and Save to file the outcome of the Total Votes
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------\n")
    # Print the final vote count to the terminal
    print(election_results, end="")
    #Save the final vote count to the text file
    txt_file.write(election_results)
    
    # Print and Save to file the Vote outcome by Candidate
    for candidate_name in candidate_votes:
        # Retrieve candidate vote count and percentage
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100        
        candidate_results = (f"{candidate_name}:  {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidates name, vote count, and % of votes to the terminal        
        print(candidate_results)
        #Save the candidate's results to the text file
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):        
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
        # Print the winning candidates' results to the terminal
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------\n")
    print(winning_candidate_summary)
    #Save the candidate's results to the text file
    txt_file.write(winning_candidate_summary)


