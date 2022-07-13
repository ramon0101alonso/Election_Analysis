# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file

#add our dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

#adding hello world to election_analysis text
#create a filename variable to a direct or inderect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
#Write some data to file.
outfile.write("Hello World")

#Close the file
outfile.close()

#create a f ilename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:


        #write some dat to the file.
        txt_file.write("Counties in the Election\n")
        txt_file.write("--------------------------\n")
        #Write three counties to the file.
        txt_file.write("Arapahoe,\n")
        txt_file.write("Denver,\n ")
        txt_file.write("Jefferson,\n")
        txt_file.write("Ara\nDen\nJef")

#the code below is the assigment code

        # Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote couter.
total_votes = 0

#Candidate Options
candidate_options = []
#1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

    #Print each row in the CSV file.
    for row in file_reader:
        print(row)
        #Add to the total vote count.
        total_votes += 1
        #Print the candidate name from each row
        candidate_name = row[2]

        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's vote count.
        candidate_votes[candidate_name] +=1

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
#  To do: print out the winning candidate, vote count and percentage to
#   terminal.