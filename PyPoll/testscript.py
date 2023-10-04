# Import module to read csv files
import csv

#Import module to create path for operating systems
import os


# Load csv data from Resources folder
Resources_File = os.path.join("Resources", "election_data.csv")


# Create variables
# Variable to capture total number of votes cast in election, start at zero
VotesTotal = 0

# Empty list to capture names of each unique candidate in election
Candidates = [] 

# Empty dictionary where vote counts of each unique candidate will be tallied by candidate name
VotesByCandidate = {}

# Variable to capture and output name of candidate who receives most votes
ElectionWinner = ""

# Start count of votes for winning candidate at zero
WinnerVotes = 0


# Read and process csv file from Resources folder
with open(Resources_File) as Resources_Data:

    Read = csv.reader(Resources_Data)

    # Pass through the first header row
    HeaderRow = next(Read)

    # Initialize for loop to run through vote tallies 
    for row in Read:

        # For each row add a vote to the the total count
        VotesTotal += 1

        # Initialize names of each unique candidate and record votes receieved by each
        if row[2] not in Candidates:  # If this is a new name then record it
            Candidates.append(row[2])  # Add new name to Candidates list
            VotesByCandidate[row[2]] = 0   #  dictionary key: candidate name, value = 0 (initialized)

        # Add up votes as they come in for each candidate in the dictionary 
        VotesByCandidate[row[2]] = VotesByCandidate[row[2]] + 1

# Now that we have created dictionary with candidate name and number of votes received, loop through each candidate
for candidate in VotesByCandidate:

    # Tally results

    Votes = VotesByCandidate.get(candidate)  # get() gets the value for each key in dictionary, which is candidate name
    vote_percentage = float(Votes) / float(VotesTotal) * 100

    # Determine the winner of election and output number of votes winner receieved
    if (Votes > WinnerVotes):
        WinnerVotes = Votes
        ElectionWinner = candidate


    # Output results to Git Bash Terminal or Terminal in MacOS
    results_output = f"{candidate}: {vote_percentage:.3f}% ({Votes})\n"
    print(results_output)


# Print results to Git Bash Terminal or Terminal in MacOS
Election_Results = (

    f"\n\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {VotesTotal}\n"
    f"-------------------------\n")

print(Election_Results)


# Print summary of election winner to Terminal
Election_Results_Summary = (

    f"-------------------------\n"
    f"Winner: {ElectionWinner}\n"
    f"-------------------------\n")

print(Election_Results_Summary)


# Write Election_Results from terminal to txt file in Analysis folder
output_file = os.path.join("Analysis", "election_results.txt")

# Print the results and export the data to .txt file
with open(output_file, "w") as txt_file:

    # Save the final vote count to the text file
    txt_file.write(Election_Results)


# Write summary fo the Winning Candidate to .txt file
output_file = os.path.join("Analysis", "winning_candidate_summary.txt")


# Print the results and export the data to .txt file
with open(output_file, "w") as txt_file:

    # Save the winning candidate's name to the text file in Analysis folder
    txt_file.write(Election_Results_Summary)