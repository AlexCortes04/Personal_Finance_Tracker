import json
import pandas as pd

def display_main_menu_and_get_choice():
    print("=== Personal Finance Tracker ===\n"
          "0. Load previous session\n"
          "1. Import a CSV File\n"
          "2. View All Transactions\n"
          "3. View Transactions by Date Range\n"
          "4. Add a Transaction\n"
          "5. Edit a Transaction\n"
          "6. Delete a Transaction\n"
          "7. Spending by Category (Current Month)\n"
          "8. Current Month Total Spending\n"
          "9. Rank Spending Categories (Current Month)\n"
          "10. Visualize Monthly Spending Trend\n"
          "11. Historical Monthly Spending by Category\n"
          "12. Save Transactions to CSV\n"
          "13. Exit")
    choice = input("Choose an option (0-13): ")
    if choice.isdigit() and 0 <= int(choice) <= 13:
        return int(choice)
    else:
        print("Invalid choice, please try again.")
        return display_main_menu_and_get_choice()
