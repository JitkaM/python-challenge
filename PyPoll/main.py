import csv
import operator

total_votes = 0
candidates_dict = {}
vote_count = 0

with open('election_data.csv', 'r') as csvfile:
    filereader = csv.reader(csvfile)
    next(filereader)
    for row in filereader:
        total_votes += 1
        if row[2] in candidates_dict:
            vote_count = candidates_dict[row[2]]
            vote_count += 1
        else:

            vote_count = 1
        candidates_dict[row[2]] = vote_count

candidates_sorted_list = sorted(candidates_dict.items(), key=operator.itemgetter(1), reverse=True)

print("Election Results")
print("----------------------------")
print("Total Votes: " + str(total_votes))
print("----------------------------")
for i in range(len(candidates_sorted_list)):
    print(candidates_sorted_list[i][0] + ": " + str(round(((candidates_sorted_list[i][1]/total_votes)*100),3)) + "% " + "(" + str(candidates_sorted_list[i][1]) + ")")
print("----------------------------")
print("Winner: "+ candidates_sorted_list[0][0])
print("----------------------------")

with open('pypoll_jmf.txt','w') as out:
    out.write("Election Results\n")
    out.write("----------------------------\n")
    out.write("Total Votes: " + str(total_votes) + "\n")
    out.write("----------------------------\n")
    for i in range(len(candidates_sorted_list)):
        out.write(candidates_sorted_list[i][0] + ": " + str(round(((candidates_sorted_list[i][1]/total_votes)*100),3)) + "% " + "(" + str(candidates_sorted_list[i][1]) + ")\n")
    out.write("----------------------------\n")
    out.write("Winner: "+ candidates_sorted_list[0][0] + "\n")
    out.write("----------------------------")