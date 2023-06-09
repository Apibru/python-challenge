import csv
import os
file_path = os.path.join('Resources', 'budget_data.csv')
with open(file_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    TotalMonths = 0.

    #The net total amount of "Profit/Losses" over the entire period
    TotalProfitLosses = 0
    for row in reader:
     TotalMonths += 1
     TotalProfitLosses += int(row[1])

print(TotalMonths)
print (TotalProfitLosses)
    

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

# Initialize variables
total_change_profits = 0
previous_profit_loss = 0
change_profits = 0
count = 0

# Open file
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through rows in file
    for row in csvreader:
        count += 1
        current_profit_loss = int(row[1])
        if count == 1:
            previous_profit_loss = current_profit_loss
        else:
            change_profits = current_profit_loss - previous_profit_loss
            total_change_profits += change_profits
            previous_profit_loss = current_profit_loss

# Calculate the average change in profits
average_change_profits = (total_change_profits / (count - 1))

#The greatest increase in profits (date and amount) over the entire period
# Initialize variables

greatest_increase_profits = 0
previous_profit_loss = 0
date_greatest_increase_profits = ""

# Open file
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through rows in file
    for row in csvreader:
        current_profit_loss = int(row[1])
        if previous_profit_loss == 0:
            previous_profit_loss = current_profit_loss
            continue
        else:
            change_profits = current_profit_loss - previous_profit_loss
            if change_profits > greatest_increase_profits:
                greatest_increase_profits = change_profits
                date_greatest_increase_profits = row[0]
            previous_profit_loss = current_profit_loss

print(f"The greatest increase in profits was {greatest_increase_profits} on {date_greatest_increase_profits}")


#The greatest decrease in profits (date and amount) over the entire period

# Initialize variables
greatest_decrease_profits = 0
previous_profit_loss = 0
date_greatest_decrease_profits = ""

# Open file
with open(file_path, newline='') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through rows in file
    for row in csvreader:
        current_profit_loss = int(row[1])
        if previous_profit_loss == 0:
            previous_profit_loss = current_profit_loss
            continue
        else:
            change_profits = current_profit_loss - previous_profit_loss
            if change_profits < greatest_decrease_profits:
                greatest_decrease_profits = change_profits
                date_greatest_decrease_profits = row[0]
            previous_profit_loss = current_profit_loss

print(f"The greatest decrease in profits was {greatest_decrease_profits} on {date_greatest_decrease_profits}")