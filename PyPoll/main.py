import csv

#bring in csv file
print("Loading results...\n")
with open ("election_data.csv","r") as election_file:
    election_data = csv.reader(election_file,delimiter = ',')
    
    next(election_data)
    election_data = list(election_data)

    #calculate total number of votes
    total_votes = sum(1 for row in election_data)

    #provide list of candidates 
    candidates = []
    [candidates.append(row[2]) for row in election_data if row[2] not in candidates]
    
    #calculate numbers of votes per candidate
    candidate_votes0 = sum(1 for row in election_data if row[2] == candidates[0])
    candidate_votes1 = sum(1 for row in election_data if row[2] == candidates[1])
    candidate_votes2 = sum(1 for row in election_data if row[2] == candidates[2])
    candidate_votes3 = sum(1 for row in election_data if row[2] == candidates[3])

    #calculate percentage of votes each candidate won
    perc_votes0 = round((candidate_votes0/total_votes)*100,4)
    perc_votes1 = round((candidate_votes1/total_votes)*100,4)
    perc_votes2 = round((candidate_votes2/total_votes)*100,4)
    perc_votes3 = round((candidate_votes3/total_votes)*100,4)

    #store values in dictionary
    election_dict = {
        "total votes": total_votes,
        'first_candidate': {
            'name': candidates[0],
            'percentage':perc_votes0,
            'total': candidate_votes0
        },
        'second_candidate':{
            'name': candidates[1],
            'percentage': perc_votes1,
            'total':candidate_votes1
        },
        'third_candidate':{
            'name': candidates[2],
            'percentage':perc_votes2,
            'total':candidate_votes2
        },
        'fourth_candidate':{
            'name':candidates[3],
            'percentage':perc_votes3,
            'total':candidate_votes3
        }
    }

    #print results
    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {election_dict["total votes"]}')
    print("-------------------------")
    print(f'{election_dict["first_candidate"]["name"]}: {election_dict["first_candidate"]["percentage"]}% ({election_dict["first_candidate"]["total"]})')
    print(f'{election_dict["second_candidate"]["name"]}: {election_dict["second_candidate"]["percentage"]}% ({election_dict["second_candidate"]["total"]})')
    print(f'{election_dict["third_candidate"]["name"]}: {election_dict["third_candidate"]["percentage"]}% ({election_dict["third_candidate"]["total"]})')
    print(f'{election_dict["fourth_candidate"]["name"]}: {election_dict["fourth_candidate"]["percentage"]}% ({election_dict["fourth_candidate"]["total"]})')
    print("-------------------------")
    
    #find winner of election based on popular vote 
    if candidate_votes0 > candidate_votes1 and candidate_votes0 > candidate_votes2 and candidate_votes0 > candidate_votes3:
        winner = candidates[0]
        print(f'Winner: {winner}')
    elif candidate_votes1 > candidate_votes0 and candidate_votes1 > candidate_votes2 and candidate_votes1 > candidate_votes3:
        winner = candidates[1]
        print(f'Winner: {winner}')
    elif candidate_votes2 > candidate_votes0 and candidate_votes2 > candidate_votes1 and candidate_votes2 > candidate_votes3:
        winner = candidates[2]
        print(f'Winner: {winner}')
    else:
        winner = candidates[3]
        print(f'Winner: {winner}')
    print("-------------------------")
    print("File 'votingresults.txt' has been exported.")
    
    #export to text file
    with open("votingresults.txt","w") as voting_results:
        voting_results.write("Election Results\n-------------------------")
        voting_results.write(f'\nTotal Votes: {election_dict["total votes"]}\n-------------------------')
        voting_results.write(f'\n{election_dict["first_candidate"]["name"]}: {election_dict["first_candidate"]["percentage"]}% ({election_dict["first_candidate"]["total"]})')
        voting_results.write(f'\n{election_dict["second_candidate"]["name"]}: {election_dict["second_candidate"]["percentage"]}% ({election_dict["second_candidate"]["total"]})')
        voting_results.write(f'\n{election_dict["third_candidate"]["name"]}: {election_dict["third_candidate"]["percentage"]}% ({election_dict["third_candidate"]["total"]})')
        voting_results.write(f'\n{election_dict["fourth_candidate"]["name"]}: {election_dict["fourth_candidate"]["percentage"]}% ({election_dict["fourth_candidate"]["total"]})\n-------------------------')
        voting_results.write(f'\nWinner: {winner}\n-------------------------')
