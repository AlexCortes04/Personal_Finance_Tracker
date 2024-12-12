from view import show_initial_menu
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import WindowsPath


class Finances:
    def __init__(self):
        self.date = None
        self.category = None
        self.description = None
        self.amount = None
        self.data = None

    def start(self):
        # Run the initial menu under while loop
        while True:
            choice = show_initial_menu()
            while True:
                if not choice.isdecimal():
                    print("Choose one of the options in the menu")
                    choice = show_initial_menu()
                    continue

                choice = int(choice)
                if not 0 <= choice <= 12:
                    print("Enter a number from 0 to 12")
                    choice = show_initial_menu()
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
                    self.spending_by_category_to_date()
                case 7:
                    self.monthly_spend_to_date()
                case 8:
                    self.rank_spending_category_to_date()
                case 9:
                    self.plot_monthly_spending()
                case 10:
                    self.historical_monthly_spending()
                case 11:
                    self.save_csv()
                case 12:
                    print("Exiting the Personal Finance Tracker. Goodbye!")
                    exit()

    def import_csv(self):
        input_path = input("Enter file path: ")
        # Remove extra quotes
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
        # Ensure 'Date' is in datetime format
        self.data['Date'] = pd.to_datetime(self.data['Date'], format='%Y-%m-%d')

        # Set the date range for further validation
        min_range = str(self.data['Date'].dt.date.min())  # Transform into str type to compare with input
        max_range = str(self.data['Date'].dt.date.max())

        print(f"Select a valid date range between {min_range} to {max_range}")
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        end_date = input("Enter the end date (YYYY-MM-DD): ")
        if (start_date >= min_range) & (end_date <= max_range):
            # Filter data between two dates
            filtered_df = self.data.loc[(self.data['Date'] >= start_date)
                                        & (self.data['Date'] < end_date)]

            # Display transaction in inputted range
            print(f"--- Transactions from {start_date} to {end_date} ---")
            print(filtered_df)
        else:
            print("No transactions found in this date range.")

    def add_transaction(self):
        # List to store user input
        new_row = []

        date = input("Enter the date (YYYY-MM-DD): ")
        new_row.append(date)
        category = input("Enter the category (e.g., Food, Rent): ")
        new_row.append(category)
        description = input("Enter a description: ")
        new_row.append(description)
        amount = input("Enter the amount: ")
        new_row.append(float(amount)) # Ensure it is stored as float
        type_x = input("Enter the type ('Expense' or 'Income'): ")
        new_row.append(type_x)

        # Display recently added transaction details
        print("Transaction added successfully!\n")
        self.data.loc[len(self.data)] = new_row

    def edit_transaction(self):
        index_row = int(input("Enter the index of the transaction to edit: "))
        if index_row in self.data.index:
            # Display current details
            print("Current Transaction Details:")
            print(self.data.loc[index_row])
        else:
            print("Invalid index")

        date = input("Enter new date (YYYY-MM-DD) or press Enter to keep current: ")
        # If user input a value, changes occur
        if date:
            self.data.loc[index_row, 'Date'] = date
        category = input("Enter new category or press Enter to keep current: ")
        if category:
            self.data.loc[index_row, 'Category'] = category
        description = input("Enter new description or press Enter to keep current: ")
        if description:
            self.data.loc[index_row, 'Description'] = description
        amount = input("Enter new amount or press Enter to keep current: ")
        if amount:
            self.data.loc[index_row, 'Amount'] = float(amount)  # Ensure it is converted to float
        type_x = input("Enter the type ('Expense' or 'Income'): ")
        if type_x:
            self.data.loc[index_row, 'Type'] = type_x

        # Confirm update
        print("Transaction updated successfully!")
        print(self.data.loc[index_row])

    def delete_transaction(self):
        index_row = int(input("Enter the index of the transaction to delete: "))

        if index_row in self.data.index:
            # Display current details
            print("Transaction Details:")
            print(self.data.loc[index_row])

            # Confirm before definitely remove the record
            confirm = input("Are you sure you wanna delete this record? (Y/N): ")
            if confirm.upper() == 'Y':
                self.data.drop(index=index_row, inplace=True)
                self.data.reset_index(drop=True, inplace=True)
                print("Transaction deleted successfully!")
            else:
                print("Deletion canceled.")
        else:
            print("Invalid index")

    def spending_by_category_to_date(self):
        # Ensure 'Date' is in datetime format
        self.data['Date'] = pd.to_datetime(self.data['Date'], format='%Y-%m-%d')

        print("--- Total Spending by Category (Current Month to Date) ---\n")

        # Filter data for the current month
        today = pd.Timestamp.now()
        current_month_data = self.data[
            (self.data['Date'].dt.month == today.month) &
            (self.data['Date'].dt.year == today.year)]

        # Group by category and sum amounts
        spending = current_month_data.groupby('Category')['Amount'].sum()

        # Indicator whether grouped df is empty
        if not spending.empty:
            print(spending)
        else:
            print("No transactions recorded for the current month.")

    def monthly_spend_to_date(self):
        # Ensure 'Date' is in datetime format
        self.data['Date'] = pd.to_datetime(self.data['Date'], format='%Y-%m-%d')

        print("--- Current Cumulated Spending by Month---")

        # Calculate spending for the current month
        today = pd.Timestamp.now()
        current_month_data = self.data[
            (self.data['Date'].dt.month == today.month) &
            (self.data['Date'].dt.year == today.year)
            ]
        current_month_spending = current_month_data['Amount'].sum()
        print(
            f"Current Month Spending (from {today.replace(day=1).date()} to {today.date()}): {current_month_spending:.2f}")

    def rank_spending_category_to_date(self):
        # Ensure 'Date' is in datetime format
        self.data['Date'] = pd.to_datetime(self.data['Date'], format='%Y-%m-%d')

        # Filter data for the current month
        today = pd.Timestamp.now()
        current_month_data = self.data[
            (self.data['Date'].dt.month == today.month) &
            (self.data['Date'].dt.year == today.year)
            ]

        # Group by category and sum amounts
        spending = current_month_data.groupby('Category')['Amount'].sum()

        # Rank categories by total spending (descending)
        ranked_spending = spending.sort_values(ascending=False)

        # Display ranked categories
        print("Rank of spending categories to date\n")
        if not ranked_spending.empty:
            for rank, (category, amount) in enumerate(ranked_spending.items(), start=1):
                print(f"{rank}. {category}: {amount:.2f}")

    def plot_monthly_spending(self):
        # Ensure 'Date' is in datetime format
        self.data['Date'] = pd.to_datetime(self.data['Date'], format='%Y-%m-%d')

        # Extract year and month for grouping
        self.data['YearMonth'] = self.data['Date'].dt.to_period('M')

        # Group by YearMonth and calculate total spending
        monthly_spending = self.data.groupby('YearMonth')['Amount'].sum()

        # Plot the line chart
        plt.figure(figsize=(10, 6))
        monthly_spending.plot(kind='line', marker='o', color='blue', linestyle='-', linewidth=2)
        plt.title("Monthly Spending Trend", fontsize=16)
        plt.xlabel("Month", fontsize=12)
        plt.ylabel("Total Spending", fontsize=12)
        plt.xticks(rotation=45)
        plt.grid(alpha=0.5)
        plt.tight_layout()

        # Show the plot
        plt.show()

    def historical_monthly_spending(self):
        # Ensure 'Date' is in datetime format
        self.data['Date'] = pd.to_datetime(self.data['Date'], format='%Y-%m-%d')

        print("--- Spending by Category (Each Month) ---\n")

        # Extract Year-Month for grouping
        self.data['YearMonth'] = self.data['Date'].dt.to_period('M')

        # Group by 'YearMonth' and 'Category', summing amounts
        monthly_spending = self.data.groupby(['YearMonth', 'Category'])['Amount'].sum()

        # Reset index for display purposes
        monthly_spending = monthly_spending.reset_index()

        # Indicator whether grouped df is empty
        if not monthly_spending.empty:
            for month in monthly_spending['YearMonth'].unique():
                print(f"{month}:")
                month_data = monthly_spending[monthly_spending['YearMonth'] == month]
                for _, row in month_data.iterrows():
                    print(f"  {row['Category']}: {row['Amount']:.2f}")
        else:
            print("No transactions recorded.")

    def save_csv(self):
        file_name = input("Enter file name to save (e.g., 'transactions.csv'): ")

        # Save the DataFrame to a CSV file
        try:
            self.data.to_csv(file_name, index=False)
            print(f"Transactions saved to {file_name} successfully!")
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")


f = Finances()
f.start()
