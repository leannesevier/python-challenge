#PyBank
# Import os module to create file path accross operating systems
import os

# Module for reading csv file
import csv

csvpath = os.path.join('budget_data.csv')

 #Reading using csv module
with open(csvpath, newline='') as csvfile:

#csv specifies delimiter and variable that holds content
 csvreader = csv.reader(csvfile, delimiter=",")

 #read the header row first
 csv_header = next(csvreader)

 # Create list to store data
 profit = []
 monthly_changes = []
 date = []
 count = 0
 total_profit =  0
 total_change_profits = 0
 initial_profit = 0

 # Conduct Ask
 for row in csvreader:
   # Use count to count the number months in this dataset
   count = count + 1

   # Will need it when collecting the greatest increase and decrease in profits
   date.append(row[0])

   # Append the profit information & calculate the total profit
   profit.append(row[1])

   total_profit = total_profit + int(row[1])

   # Calculate the average change in profits from month to month. Then calulate the average change in profits
   final_profit = int(row[1])

   monthly_change_profits = final_profit - initial_profit

   # Store these monthly changes in a list
   monthly_changes.append(monthly_change_profits)

   total_change_profits = total_change_profits + monthly_change_profits

   initial_profit = final_profit

   # Calculate the average change in profits

   average_change_profits = round(total_change_profits / count,2)

   # Find the max and min change in profits and the corresponding dates these changes were obeserved

   greatest_increase_profits = max(monthly_changes)

   greatest_decrease_profits = min(monthly_changes)

   increase_date = date[monthly_changes.index(greatest_increase_profits)]

   decrease_date = date[monthly_changes.index(greatest_decrease_profits)]

   print("----------------------------------------------------------")
   print("Financial Analysis")
   print("----------------------------------------------------------")
   print(f"Total Months:{count}")
   print(f"Total Profits:  $ {total_profit}")
   print(f"Average Change:  $ {average_change_profits}")
   print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase_profits})")
   print(f"Greatest Decrease in Profits: {increase_date} (${greatest_decrease_profits})")
   print("----------------------------------------------------------")

   with open('financial_analysis.txt', 'w') as text:
     text.write("----------------------------------------------------------\n")
     text.write("  Financial Analysis" + "\n")
     text.write("----------------------------------------------------------\n\n")
     text.write(f"Total Months:{count}" + "\n")
     text.write(f"Total Profits:  $ {total_profit}" + "\n")
     text.write(f"Average Change:  $ {average_change_profits}" + "\n")
     text.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase_profits})" + "\n")
     text.write(f"Greatest Decrease in Profits: {increase_date}  (${greatest_decrease_profits})" + "\n")
     text.write("----------------------------------------------------------\n")