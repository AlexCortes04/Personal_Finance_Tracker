import pandas as pd
from model.io_handler import read_csv, write_csv


class Finances:
    def __init__(self):
        self.data = None

    def import_data(self, path):
        self.data = read_csv(path)

    def get_all_transactions(self):
        return self.data

    def ensure_dates_are_datetime(self):
        if self.data is not None and self.data['Date'].dtype != '<M8[ns]':
            self.data['Date'] = pd.to_datetime(self.data['Date'], format='%Y-%m-%d', errors='coerce').dt.date

    def get_min_max_dates(self):
        if self.data is None:
            return None, None
        min_date = str(self.data['Date'].min().date())
        max_date = str(self.data['Date'].max().date())
        return min_date, max_date

    def add_transaction(self, date, category, description, amount, transaction_type):
        new_row = [date, category, description, float(amount), transaction_type]
        self.data.loc[len(self.data)] = new_row

    def edit_transaction(self, index, date, category, description, amount, transaction_type):
        if date:
            self.data.loc[index, 'Date'] = date
        if category:
            self.data.loc[index, 'Category'] = category
        if description:
            self.data.loc[index, 'Description'] = description
        if amount:
            self.data.loc[index, 'Amount'] = float(amount)
        if transaction_type:
            self.data.loc[index, 'Type'] = transaction_type

    def delete_transaction(self, index):
        self.data.drop(index=index, inplace=True)
        self.data.reset_index(drop=True, inplace=True)

    def save_data(self, filename):
        write_csv(self.data, filename)
