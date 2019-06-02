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
difference = budget_file["Profit/Losses"].shift(1)
initial = budget_file["Profit/Losses"]
average = (initial - difference).mean()
print(f'Average Change: ${average}')

# calculate greatest increase in profits (date and amount) over entire period
increase = (initial - difference).max()
print(increase)
print(budget_file.loc[df["Profit/Losses"]])

# greatest decrease in losses (date and amount) over entire period 
decrease = (initial - difference).min()
print(decrease)