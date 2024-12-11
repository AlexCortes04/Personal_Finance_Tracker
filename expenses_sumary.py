from view import show_initial_menu
from analysis import spending_by_category, monthly_spending, top_spending_category, plot_monthly_spending
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import WindowsPath
import datetime


class Finances:
    def __init__(self):
        self.date = None
        self.category = None
        self.description = None
        self.amount = None
        self.data = None

    def start(self):
        while True:
            choice = show_initial_menu()
            while True:
                if not choice.isdecimal():
                    print("Choose one of the options in the menu")
                    continue

                choice = int(choice)
                if not 0 <= choice <= 11:
                    print("Enter a number from 0 to 5")
                    continue
                break

            match choice:
                case 0:
                    self.import_csv()
                case 1:
                    self.view_transactions()
                case 2:
                    self.view_transaction_date_range()
                case 3:
                    self.add_transaction()
                case 4:
                    self.edit_transaction()
                case 5:
                    self.delete_transaction()
                case 6:
                    spending_by_category()
                case 7:
                    monthly_spending()
                case 8:
                    top_spending_category()
                case 9:
                    plot_monthly_spending()
                case 10:
                    pass
                case 11:
                    print("Exiting the Personal Finance Tracker. Goodbye!")
                    exit()


    def import_csv(self):
        input_path = input("Enter file path: ")
        path = WindowsPath(input_path.replace('"', ''))

        if input_path == self.data:
            input("The file is already uploaded, type a valid file path")

        try:
            self.data = pd.read_csv(path)
            print("Data successfully load\n")
        except Exception as e:
            print(f"Error loading data: {e}")

        return

    def view_transactions(self):
        if self.data is None:
            print("Data not loaded. Import csv file, first")

        print("--- All Transactions ---\n")
        print(self.data)

    def view_transaction_date_range(self):
        # Convert the date to datetime64
        self.data['Date'] = pd.to_datetime(self.data['Date'], format='%Y-%m-%d')

        # Set the date range for further validation
        min_range = str(self.data['Date'].dt.date.min())
        max_range = str(self.data['Date'].dt.date.max())

        print(f"Select a valid date range between {min_range} to {max_range}")
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        end_date = input("Enter the end date (YYYY-MM-DD): ")
        if (start_date >= min_range) & (end_date <= max_range):
            # Filter data between two dates
            filtered_df = self.data.loc[(self.data['Date'] >= start_date)
                                   & (self.data['Date'] < end_date)]
            print(f"--- Transactions from {start_date} to {end_date} ---")
            print(filtered_df)
        else:
            print("No transactions found in this date range.")

    def add_transaction(self):
        new_row = []
        date = input("Enter the date (YYYY-MM-DD): ")
        new_row.append(date)
        category = input("Enter the category (e.g., Food, Rent): ")
        new_row.append(category)
        description = input("Enter a description: ")
        new_row.append(description)
        amount = input("Enter the amount: ")
        new_row.append(amount)
        type = input("Enter the type ('Expense' or 'Income'): ")
        new_row.append(type)
        # seller
        # payment method

        self.data.loc[len(self.data)] = new_row
        print("Transaction added successfully!")

    def edit_transaction(self):
        index_row = int(input("Enter the index of the transaction to edit: "))
        if index_row in self.data.index:
            print(self.data.loc[index_row])
        else:
            print("Invalid index")

        date = input("Enter new date (YYYY-MM-DD) or press Enter to keep current: ")
        if not date == "":
            self.data.loc[index_row, 'Date'] = date
        category = input("Enter new category or press Enter to keep current: ")
        if not date == "":
            self.data.loc[index_row, 'Category'] = category
        description = input("Enter new description or press Enter to keep current: ")
        if not date == "":
            self.data.loc[index_row, 'Description'] = description
        amount = input("Enter new amount or press Enter to keep current: ")
        if not date == "":
            self.data.loc[index_row, 'Amount'] = amount
        type = input("Enter the type ('Expense' or 'Income'): ")
        if not date == "":
            self.data.loc[index_row, 'Type'] = type

        print(self.data.loc[index_row])
        print("Transaction updated successfully!")

    def delete_transaction(self):
        index_row = int(input("Enter the index of the transaction to delete: "))
        if index_row in self.data.index:
            print(self.data.loc[index_row])
            self.data.drop(index=index_row)
            print("Transaction deleted successfully!")
        else:
            print("Invalid index")


f = Finances()
f.start()
