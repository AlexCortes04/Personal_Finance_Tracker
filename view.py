@staticmethod
def show_initial_menu():
    print("=== Personal Finance Tracker ===\n"
        "0. Import a CSV File\n"
        "1. View All Transactions\n"
        "2. View Transactions by Date Range\n"
        "3. Add a Transaction\n"
        "4. Edit a Transaction\n"
        "5. Delete a Transaction\n"
        "6. Spending by Category to date\n"
        "7. Average Monthly Spending to date\n"
        "8. Show Rank Spending Category\n"
        "9. Visualize Monthly Spending Trend\n"
        "10. Show historical monthly spending\n" 
        "11. Save Transactions to CSV\n"
        "12. Exit"
          )
    return input("Choose an option (0-12):")
