import csv


file_input =  "election_data.csv"
file_output = "election_analysis.txt"

total_votes = 0
candidates = {}
candidates_percent = {}
winner_count = 0
winner = ""


with open(file_input, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)
    for row in csvreader:
        
        total_votes += 1
        
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

     
        for key,Value in candidates.items():
            candidates_percent[key] = round((value/total_votes) * 100, 1)

        for key in candidates.keys():
          if candidates[key] > winner_count
        winner = candidates[winner_count]



with open(file_output, 'w') as file:
    file.write("Election Results \n")
    file.write("------------------------------------- \n")
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("------------------------------------- \n")
    for key, value in candidates.items():
    file.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ") \n")
    file.write("------------------------------------- \n")
    file.write("Winner: " + winner + "\n")
    file.write("------------------------------------- \n")