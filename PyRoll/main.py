import csv

file_input =  "election_data.csv"
file_output = "election_analysis.txt"

candidates = []
num_votes = 0
vote_counts = []

with open(file_input,newline="") as csvfile:
    csvreader = csv.reader(csvfile)

    line = next(csvreader,None)

    for line in csvreader:

    
        num_votes = num_votes + 1

    
        candidate = line[2]

    
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        
        else:
            candidates.append(candidate)
            vote_counts.append(1)

percentages = []
max_votes = vote_counts[0]
max_index = 0

for count in range(len(candidates)):
    vote_percentage = vote_counts[count]/num_votes*100
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]

#print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {num_votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

write_file = f"election_analysis.txt"

filewriter = open(write_file, mode = 'w')

filewriter.write("Election Results\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total Votes: {num_votes}\n")
for count in range(len(candidates)):
    filewriter.write(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})\n")
filewriter.write("---------------------------\n")
filewriter.write(f"Winner: {winner}\n")
filewriter.write("---------------------------\n")
