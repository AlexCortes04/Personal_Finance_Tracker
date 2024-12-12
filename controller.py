from view.menu import display_main_menu_and_get_choice
from view.display import (
    display_message,
    display_all_transactions,
    display_transactions_within_range,
    display_current_month_spending_by_category,
    display_current_month_spending_total,
    display_current_month_category_ranking,
    display_historical_monthly_spending_by_category
)
from model.finances import Finances
from analytics import (
    filter_transactions_within_date_range,
    calculate_current_month_spending_by_category,
    calculate_current_month_total_spending,
    rank_spending_categories_current_month,
    calculate_historical_monthly_spending_by_category
)
from plotting import plot_monthly_spending_over_time

import sys
import json
import pandas as pd


class PersonalFinanceController:
    def __init__(self):
        self.finances = Finances()

    def run(self):
        while True:
            choice = display_main_menu_and_get_choice()
            if choice == 0:
                self.import_csv_data()
            elif choice == 1:
                self.load_previous_session()
            elif choice == 2:
                self.display_all_transactions()
            elif choice == 3:
                self.display_transactions_by_date_range()
            elif choice == 4:
                self.add_new_transaction()
            elif choice == 5:
                self.edit_existing_transaction()
            elif choice == 6:
                self.delete_existing_transaction()
            elif choice == 7:
                self.display_spending_by_category_current_month()
            elif choice == 8:
                self.display_current_month_total_spending()
            elif choice == 9:
                self.display_spending_category_ranking_current_month()
            elif choice == 10:
                self.display_monthly_spending_trend_plot()
            elif choice == 11:
                self.display_historical_monthly_category_spending()
            elif choice == 12:
                self.save_session()
            elif choice == 13:
                self.save_transactions_to_csv()
            elif choice == 14:
                display_message("Exiting the Personal Finance Tracker. "
                                "Goodbye!")
                sys.exit()

    def import_csv_data(self):
        file_path = input("Enter file path: ")
        try:
            self.finances.import_data(file_path)
            display_message("Data successfully loaded.\n")
        except Exception as e:
            display_message(f"Error loading data: {e}\n")

    def load_previous_session(self):
        pass

    def display_all_transactions(self):
        data = self.finances.get_all_transactions()
        if data is not None:
            display_all_transactions(data)
        else:
            display_message("Data not loaded. Import a CSV file first.\n")

    def display_transactions_by_date_range(self):
        data = self.finances.get_all_transactions()
        if data is None:
            display_message("Data not loaded. Import a CSV file first.\n")
            return

        self.finances.ensure_dates_are_datetime()

        min_date, max_date = self.finances.get_min_max_dates()
        print(f"Select a valid date range between {min_date} and {max_date}")
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        end_date = input("Enter the end date (YYYY-MM-DD): ")

        filtered = filter_transactions_within_date_range(data, start_date, end_date)
        display_transactions_within_range(filtered, start_date, end_date)

    def add_new_transaction(self):
        if self.finances.get_all_transactions() is None:
            display_message("Data not loaded. Import a CSV file first.\n")
            return

        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the category (e.g., Food, Rent): ")
        description = input("Enter a description: ")
        amount = input("Enter the amount: ")
        transaction_type = input("Enter the type ('Expense' or 'Income'): ")

        try:
            self.finances.add_transaction(date, category, description, amount, transaction_type)
            display_message("Transaction added successfully!\n")
        except Exception as e:
            display_message(f"Error adding transaction: {e}\n")

    def edit_existing_transaction(self):
        data = self.finances.get_all_transactions()
        if data is None:
            display_message("Data not loaded. Import a CSV file first.\n")
            return

        try:
            index = int(input("Enter the index of the transaction to edit: "))
        except ValueError:
            display_message("Invalid index.\n")
            return

        if index not in data.index:
            display_message("Invalid index.\n")
            return

        display_message("Current Transaction Details:")
        display_message(str(data.loc[index]) + "\n")

        date = input("Enter new date (YYYY-MM-DD) or press Enter to keep current: ")
        category = input("Enter new category or press Enter to keep current: ")
        description = input("Enter new description or press Enter to keep current: ")
        amount = input("Enter new amount or press Enter to keep current: ")
        transaction_type = input("Enter new type ('Expense' or 'Income') or press Enter to keep current: ")

        self.finances.edit_transaction(index, date, category, description, amount, transaction_type)
        display_message("Transaction updated successfully!")
        display_message(str(data.loc[index]) + "\n")

    def delete_existing_transaction(self):
        data = self.finances.get_all_transactions()
        if data is None:
            display_message("Data not loaded. Import a CSV file first.\n")
            return

        try:
            index = int(input("Enter the index of the transaction to delete: "))
        except ValueError:
            display_message("Invalid index.\n")
            return

        if index not in data.index:
            display_message("Invalid index.\n")
            return

        display_message("Transaction Details:")
        display_message(str(data.loc[index]) + "\n")

        confirm = input("Are you sure you want to delete this record? (Y/N): ")
        if confirm.strip().upper() == 'Y':
            self.finances.delete_transaction(index)
            display_message("Transaction deleted successfully!\n")
        else:
            display_message("Deletion canceled.\n")

    def display_spending_by_category_current_month(self):
        data = self.finances.get_all_transactions()
        if data is None:
            display_message("Data not loaded. Import a CSV file first.\n")
            return

        self.finances.ensure_dates_are_datetime()
        spending = calculate_current_month_spending_by_category(data)
        display_current_month_spending_by_category(spending)

    def display_current_month_total_spending(self):
        data = self.finances.get_all_transactions()
        if data is None:
            display_message("Data not loaded. Import a CSV file first.\n")
            return

        self.finances.ensure_dates_are_datetime()
        total = calculate_current_month_total_spending(data)
        display_current_month_spending_total(total)

    def display_spending_category_ranking_current_month(self):
        data = self.finances.get_all_transactions()
        if data is None:
            display_message("Data not loaded. Import a CSV file first.\n")
            return

        self.finances.ensure_dates_are_datetime()
        ranked = rank_spending_categories_current_month(data)
        display_current_month_category_ranking(ranked)

    def display_monthly_spending_trend_plot(self):
        data = self.finances.get_all_transactions()
        if data is None:
            display_message("Data not loaded. Import a CSV file first.\n")
            return

        self.finances.ensure_dates_are_datetime()
        plot_monthly_spending_over_time(data)

    def display_historical_monthly_category_spending(self):
        data = self.finances.get_all_transactions()
        if data is None:
            display_message("Data not loaded. Import a CSV file first.\n")
            return

        self.finances.ensure_dates_are_datetime()
        historical = calculate_historical_monthly_spending_by_category(data)
        display_historical_monthly_spending_by_category(historical)

    def save_session(self):
        data = self.finances.get_all_transactions()

        # Write json to check if there's previous file saved
        save = input("Do you want to save the current transactions (Y or N): ")
        if save.strip().upper() == "Y":
            filename = input("Enter a filename to save the session (e.g., 'transactions.csv'): ").strip()
            # Save current data to a CSV file
            try:
                self.finances.save_data(filename)
                display_message(f"Transactions saved to {filename} successfully!\n")
            except Exception as e:
                display_message(f"An error occurred while saving the file: {e}\n")

            # Save session state to a configuration file
            conf = {"saved": True, "filename": filename}
            with open("config.json", "w") as config_file:
                json.dump(conf, config_file, indent=4)
            print("Session state saved.")

        else:
            # Update configuration to indicate no session saved
            conf = {"saved": False}
            with open("config.json", "w") as config_file:
                json.dump(conf, config_file, indent=4)
            print("No session saved.")

    def save_transactions_to_csv(self):
        data = self.finances.get_all_transactions()
        if data is None:
            display_message("No data to save. Import a CSV file first.\n")
            return

        file_name = input("Enter file name to save (e.g., "
                          "'transactions.csv'): ").strip()
        try:
            self.finances.save_data(file_name)
            display_message(f"Transactions saved to {file_name} successfully!\n")
        except Exception as e:
            display_message(f"An error occurred while saving the file: {e}\n")
