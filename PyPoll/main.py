import csv

#bring in csv file
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

    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {election_dict["total votes"]}')
    print("-------------------------")
    print(f'{election_dict["first_candidate"]["name"]}: {election_dict["first_candidate"]["percentage"]}% ({election_dict["first_candidate"]["total"]})')
    print(f'{election_dict["second_candidate"]["name"]}: {election_dict["second_candidate"]["percentage"]}% ({election_dict["second_candidate"]["total"]})')
    print(f'{election_dict["third_candidate"]["name"]}: {election_dict["third_candidate"]["percentage"]}% ({election_dict["third_candidate"]["total"]})')
    print(f'{election_dict["fourth_candidate"]["name"]}: {election_dict["fourth_candidate"]["percentage"]}% ({election_dict["fourth_candidate"]["total"]})')
    print("-------------------------")
    
    #TODO: find winner of election based on popular vote 
    if candidate_votes0 > candidate_votes1 or candidate_votes0 > candidate_votes2 or candidate_votes0 > candidate_votes3:
        print(f'Winner: {candidates[0]}')
    elif candidate_votes1 > candidate_votes0 or candidate_votes1 > candidate_votes2 or candidate_votes1 > candidate_votes3:
        print(f'Winner: {candidates[1]}')
    elif candidate_votes2 > candidate_votes0 or candidate_votes2 > candidate_votes1 or candidate_votes2 > candidate_votes3:
        print(f'Winner: {candidates[2]}')
    else:
        print(f'Winner: {candidates[3]}')
    
    print("-------------------------")



