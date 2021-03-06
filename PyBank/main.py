import csv 

with open('budget_data.csv','r') as file:
    # read in file and skip header
    budget_data = csv.reader(file,delimiter=',')
    next(budget_data)
    budget_data = list(budget_data)

    # calculate total number of months included in dataset
    months = sum(1 for row in budget_data)

    # calculate net total amount of profit/losses over entire period
    net_total = [int(row[1]) for row in budget_data]
    net_total_sum = sum(net_total)

    # get differences in profit/losses over time
    average_change = []
    for first, second in zip(budget_data,budget_data[1:]):
        average_change.append(int(second[1]) - int(first[1]))
    
    # merge changes in profit/losses with dates
    date = []
    for row in budget_data[1:]:
        date.append(row[0])
    cleaned_csv = zip(date,average_change)

    greatest_increase = 0
    greatest_decrease = 0
    for row in cleaned_csv:
        # calculate greatest increase in profits (date and amount) over entire period
        if int(row[1]) > greatest_increase:
            increase_date = row[0]
            greatest_increase = row[1]
        # calculate greatest decrease in losses (date and amount) over entire period 
        if int(row[1]) < greatest_decrease:
            decrease_date = row[0]
            greatest_decrease = row[1]
    
    #print output to terminal
    print("Financial Analysis \n----------------------------")
    print(f'Total Months: {months}')
    print(f'Total: ${net_total_sum}')
    # calculate average of changes in profit/losses over entire period
    print(f'Average Change: ${round(sum(average_change)/len(average_change),2)}')
    print(f'Greatest Increase in Profits: {increase_date} (${greatest_increase})')
    print(f'Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})')
    print("File 'results.txt' has been exported.")
    
    #export to text file
    with open("results.txt",'w') as result_file:
        result_file.write("Financial Analysis \n----------------------------")
        result_file.write(f'\nTotal: ${net_total_sum}')
        result_file.write(f'\nAverage Change: ${round(sum(average_change)/len(average_change),2)}')
        result_file.write(f'\nGreatest Increase in Profits: {increase_date} (${greatest_increase})')
        result_file.write(f'\nGreatest Decrease in Profits: {decrease_date} (${greatest_decrease})')
