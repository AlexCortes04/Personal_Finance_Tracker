import pandas as pd

def filter_transactions_within_date_range(df, start_date, end_date):
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
    mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
    return df.loc[mask]

def calculate_current_month_spending_by_category(df):
    today = pd.Timestamp.now()
    current_month_data = df[
        (df['Date'].dt.month == today.month) &
        (df['Date'].dt.year == today.year) &
        (df['Type'] == 'Expense')
    ]
    if current_month_data.empty:
        return None
    spending = current_month_data.groupby('Category')['Amount'].sum()
    return spending

def calculate_current_month_total_spending(df):
    today = pd.Timestamp.now()
    current_month_data = df[
        (df['Date'].dt.month == today.month) &
        (df['Date'].dt.year == today.year) &
        (df['Type'] == 'Expense')
    ]
    return current_month_data['Amount'].sum()

def rank_spending_categories_current_month(df):
    today = pd.Timestamp.now()
    current_month_data = df[
        (df['Date'].dt.month == today.month) &
        (df['Date'].dt.year == today.year) &
        (df['Type'] == 'Expense')
    ]
    if current_month_data.empty:
        return None
    spending = current_month_data.groupby('Category')['Amount'].sum()
    ranked = spending.sort_values(ascending=False)
    return ranked

def calculate_historical_monthly_spending_by_category(df):
    df['YearMonth'] = df['Date'].dt.to_period('M')
    monthly_spending = df.groupby(['YearMonth', 'Category'])['Amount'].sum().reset_index()
    if monthly_spending.empty:
        return None
    return monthly_spending
