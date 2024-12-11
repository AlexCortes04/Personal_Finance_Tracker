import pandas as pd


@staticmethod
def show_initial_menu():
    print("=== Personal Finance Tracker ===\n"
        "0. Import a CSV File\n"
        "1. View All Transactions\n"
        "2. View Transactions by Date Range\n"
        "3. Add a Transaction\n"
        "4. Edit a Transaction\n"
        "5. Delete a Transaction\n"
        "6. Analyze Spending by Category\n"
        "7. Calculate Average Monthly Spending\n"
        "8. Show Top Spending Category\n"
        "9. Visualize Monthly Spending Trend\n"
        "10. Show historical monthly spending\n" 
        "11. Save Transactions to CSV\n"
        "12. Exit"
          )
    return input("Choose an option (0-12):")


data = pd.read_csv(r"C:\Users\aleec\Personal_Finance_Tracker\sampledata.csv")

print(data)

data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')
data['YearMonth'] = data['Date'].dt.to_period('M')

# Calculate spending for each month
monthly_spending = data.groupby('YearMonth')['Amount'].sum()
print("Monthly Spending:")
print(monthly_spending)


# # # Convert the date to datetime64
# # data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')
# #
# # # Set the date range for further validation
# # min_range = str(data['Date'].dt.date.min())
# # max_range = str(data['Date'].dt.date.max())
# #
# # print(f"Select a valid date range between {min_range} to {max_range}")
# # start_date = input("Enter the start date (YYYY-MM-DD): ")
# # end_date = input("Enter the end date (YYYY-MM-DD): ")
# # if (start_date >= min_range) & (end_date <= max_range):
# #     # Filter data between two dates
# #     filtered_df = data.loc[(data['Date'] >= start_date)
# #                                 & (data['Date'] < end_date)]
# #     print(f"--- Transactions from {start_date} to {end_date} ---")
# #     print(filtered_df)
# # else:
# #     print("No transactions found in this date range.")
# #
# # # print(data.dtypes)


