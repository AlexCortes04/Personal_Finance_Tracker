from view import show_initial_menu
from analysis import spending_by_category, monthly_spending, top_spending_category, plot_monthly_spending
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import WindowsPath


class Finances:
    def __init__(self):
        pass
        self.date = None
        self.category = None
        self.description = None
        self.amount = None
        self.data = None

    def start(self):
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

        try:
            self.data = pd.read_csv(path)
            print("Data successfully load")
        except Exception as e:
            print(f"Error loading data: {e}")


    def view_transactions(self):
        if self.data is None:
            print("Data not loaded. Import csv file, first")

        print("--- All Transactions ---\n")
        print(self.data)

    def view_transaction_date_range(self):
        pass

    def add_transaction(self):
        pass

    def edit_transaction(self):
        pass

    def delete_transaction(self):
        pass


f = Finances()
f.start()