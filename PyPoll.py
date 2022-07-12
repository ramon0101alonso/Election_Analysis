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

        # Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)