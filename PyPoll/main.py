import csv
import os
file_path = os.path.join('Resources', 'election_data.csv')

#with open(file_path, newline='') as csvfile:
   # reader = csv.reader(csvfile)
    #for row in reader:
       

#Total number of votes cast

# Initialize variables
total_votes = 0

# Open file
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through rows in file
    for row in csvreader:
        total_votes += 1
    print(f"The total number of votes cast is {total_votes}")


#A complete list of candidates who received votes

# Initialize variables
candidates = []

# Open file
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through rows in file
    for row in csvreader:
        candidate = row[2]
        candidates.append(candidate)

#print(f"The complete list of candidates who received votes is {candidates}")

#The percentage of votes each candidate won

# Initialize variables
total_votes = 0
candidate_votes = {}

# Open file
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through rows in file
    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        # Add candidate to dictionary if not already present
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0

        # Increment candidate's vote count
        candidate_votes[candidate] += 1

# Calculate percentage of votes for each candidate
for candidate, votes in candidate_votes.items():
    vote_percentage = (votes / total_votes) * 100
    print(f"{candidate}: {vote_percentage:.1f}%")


#The total number of votes each candidate won

# Initialize variables
total_votes = 0
candidate_votes = {}

# Open file
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through rows in file
    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        # Add candidate to dictionary if not already present
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0

        # Increment candidate's vote count
        candidate_votes[candidate] += 1

# Print total number of votes for each candidate
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {votes}")

#The winner of the election based on popular vote

# Initialize variables
total_votes = 0
candidate_votes = {}

# Open file
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through rows in file
    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        # Add candidate to dictionary if not already present
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0

        # Increment candidate's vote count
        candidate_votes[candidate] += 1

# Find winner of election based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)
print(f"The winner of the election is {winner} with {candidate_votes[winner]} votes.")
