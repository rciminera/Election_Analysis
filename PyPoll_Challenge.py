# PyPoll Homework Challenge Solution 


# Add our dependencies
import csv
import os

# Input and output files
# Assign a variable for the file to load a file from a path
file_to_load = os.path.join("Resources", '/Users/jrobertciminera/Mod3/Election_Analysis/Resources/election_results.csv')
# Assign a variable to save the file to a path
file_to_save = os.path.join("Results", '/Users/jrobertciminera/Mod3/Election_Analysis/Results/election_results.txt')

# Establish lists, dictionariies, and intitialize counters
# Initialize a total vote counter
total_votes = 0
# Candidate options list and candidate vote dictionary
candidate_options = []
candidate_votes ={}
# Winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 1: Create a county list and county votes dictionary
county_options = []
county_votes = {}

# 2: Track the largest county and county voter turnout
largest_countyname = ""
largest_countyvotes = 0
largest_countypercentage = 0

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

        # 3: Extract the county name from each row
        county_name = row[1]
        # 4a: If county does not match any existing counties add to the county list
        if county_name not in county_options:
            # 4b: Add the county name to the county list
            county_options.append(county_name)
            # 4c: And begin tracking the county's vote count
            county_votes[county_name] = 0
        # 5: Add a vote to that county's vote count
        county_votes[county_name] += 1

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
    

    # 6a: Write a for loop to get the county from the county dictionary
    for county_name in county_votes:
        # 6b: Retrieve the county vote count
        votecount = county_votes[county_name]
        # 6c: Calculate the percentage of votes for the county
        county_percentage =float(votecount) / float(total_votes) * 100
        # 6d: Print the county results to the terminal
        county_results = (
            f"{county_name}:  {county_percentage:.1f}% ({votecount:,})\n")
        print(county_results, end="")        
        # 6E: Save the county votes to a text file
        txt_file.write(county_results)

 # 6f: Write an if statement to determine the largest county and get its vote count
        if (votecount > largest_countyvotes) and (county_percentage > largest_countypercentage):        
            largest_countyvotes = votecount
            largest_county = county_name
            largest_percentage = county_percentage
        # 7: Print the largest counties' results to the terminal
    largest_county_summary = (
        f"------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"------------------------\n")
    print(largest_county_summary)
    #8: Save the largest county's results to the text file
    txt_file.write(largest_county_summary)

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

        # Determine winning candidate, vote count, and percentage
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