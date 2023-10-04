# Import module to read csv files
import csv

#Import module to create path for operating systems
import os


# Load csv data from Resources folder
Resources_File = os.path.join('Resources', "budget_data.csv")

# Create variables
# Variable to count total number of months in dataset
TotalMonths = 0

# Variable to net total amount of profits/losses over entire period
TotalProfitLoss = 0

# List of all the months in the year
MonthOfYear = []

#List of all the changes in "Profit/Losses" over the entire period
MonthlyPriceChange = []

# Variable to capture greatest increase in profits over period
BiggestProfit = ["", 0] # first element is month of year. second element is month-over-month change.

#Variable to caputre greatest decrease in profits over period
BiggestLoss = ["", 9999999999999999999] # first element is month of year. Second element is month to month change
#initially set a very high value.

# Read and process csv file from Resources folder
with open(Resources_File) as Resources_Data:
    Read = csv.reader(Resources_Data)

    
    # Read the first header row
    HeaderRow = next(Read)


    # Code to process only first line of data uniquely as it doesn't have a previous entry
    FirstRow = next(Read)
    TotalMonths += 1
    TotalProfitLoss += int(FirstRow[1])
    PrevEntry = int(FirstRow[1])  # since no line before, record the first entry as the previous entry


    # Loop through the remaining rows to the end of dataset
    for row in Read:


        # Calculate total number of months in data set and total profit/loss over time
        TotalMonths += 1
        TotalProfitLoss += int(row[1])


        # Compute the month to month changes in Profit/Losses
        MonthlyChange = int(row[1]) - PrevEntry
        PrevEntry = int(row[1]) # set the current row to PrevEntry for loop to go around again


        # Update the lists
        MonthlyPriceChange += [MonthlyChange] # add monthly change of profits/loss to list
        MonthOfYear += [row[0]] # add the values of month of year to the list
        # Calculate if the current value is higher than the previous biggest profit
        # Calculate if the current value is lower than than the previous biggest loss
       
        # Compare to previous records and record biggest rise in profits
        if MonthlyChange > BiggestProfit[1]:

            BiggestProfit[0] = row[0]
            BiggestProfit[1] = MonthlyChange


        # Compare to previous records and record biggest loss in profits
        if MonthlyChange < BiggestLoss[1]:

            BiggestLoss[0] = row[0]
            BiggestLoss[1] = MonthlyChange


# Now that monthly changes have been captured along with the highest and lowest changes
# Compute average of monthly prices changes changes over time
MonthlyChange_Average = sum(MonthlyPriceChange) / len(MonthlyPriceChange)


# Print summary of all the data collected
Summary = (

    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {TotalMonths}\n"
    f"Total Profit/Loss: ${TotalProfitLoss}\n"
    f"Average Change: ${MonthlyChange_Average:.2f}\n"
    f"Greatest Increase in Profits: {BiggestProfit[0]} (${BiggestProfit[1]})\n"
    f"Greatest Decrease in Profits: {BiggestLoss[0]} (${BiggestLoss[1]})\n"
    )


# Print summary of results to the Git Bash terminal (or terminal in MacOS)
print(Summary)


# Set location in local repository to print results of data summary
output_file = os.path.join('Analysis', "budget_data_output.txt")


# Print out data summary results to .txt file
with open(output_file, "w") as txt_file:

    txt_file.write(Summary)