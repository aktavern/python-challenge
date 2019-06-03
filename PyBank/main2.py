#import dependencies
import pandas as pd

#read file
file = "budget_data.csv"

#load file into dataframe
budget_file = pd.read_csv(file)

# calculate total number of months included in dataset
months = len(budget_file["Date"].unique())
print(f'Total Months: {months}')

# calculate net total amount of profit/losses over entire period
net_total = budget_file["Profit/Losses"].sum()
print(f'Total: {net_total}')

# calculate average of changes in profit/losses over entire period
difference = budget_file.shift(1)
average = (budget_file["Profit/Losses"] - difference["Profit/Losses"]).mean()
print(f'Average Change: ${average}')

# TODO calculate greatest increase in profits (date and amount) over entire period
increase = (budget_file["Profit/Losses"] - difference["Profit/Losses"]).max()

print(increase)
# TODO greatest decrease in losses (date and amount) over entire period 
decrease = (difference["Profit/Losses"] - budget_file["Profit/Losses"]).max()
print(decrease)