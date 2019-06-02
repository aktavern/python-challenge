import csv 

with open('budget_data.csv','r') as file:
    budget_data = csv.reader(file,delimiter=',')
    next(budget_data)
    budget_data = list(budget_data)

    # calculate total number of months included in dataset
    months = sum(1 for row in budget_data)
    print (months)
    net_total = []

    # calculate net total amount of profit/losses over entire period
    net_total = [int(row[1]) for row in budget_data]
    print(f'${sum(net_total)}')

# calculate net total amount of profit/losses over entire period
# calculate average of changes in profit/losses over entire period
# calculate greatest increase in profits (date and amount) over entire period
# greatest decrease in losses (date and amount) over entire period 