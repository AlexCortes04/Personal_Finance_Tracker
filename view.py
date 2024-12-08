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
        "10. Save Transactions to CSV\n"
        "11. Exit"
          )
    return input("Choose an option (0-11):")
