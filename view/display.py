import pandas as pd


def display_message(msg):
    print(msg)


def display_all_transactions(df):
    print("--- All Transactions ---\n")
    print(df)
    print()


def display_transactions_within_range(filtered_df, start_date, end_date):
    if filtered_df.empty:
        print("No transactions found in this date range.\n")
    else:
        print(f"--- Transactions from {start_date} to {end_date} ---")
        print(filtered_df)
        print()


def display_current_month_spending_by_category(spending):
    print("--- Total Spending by Category (Current Month) ---\n")
    if spending is None or spending.empty:
        print("No transactions recorded for the current month.\n")
    else:
        print(spending)
        print()


def display_current_month_spending_total(total):
    today = pd.Timestamp.now()
    start_of_month = today.replace(day=1).date()
    print("--- Current Month Spending ---")
    print(f"Spending from {start_of_month} to {today.date()}: {total:.2f}\n")


def display_current_month_category_ranking(ranked):
    print("Rank of Spending Categories (Current Month)\n")
    if ranked is None or ranked.empty:
        print("No spending recorded for the current month.\n")
    else:
        for i, (category, amount) in enumerate(ranked.items(), start=1):
            print(f"{i}. {category}: {amount:.2f}")
        print()


def display_historical_monthly_spending_by_category(monthly_spending):
    print("--- Historical Monthly Spending by Category ---\n")
    if monthly_spending is None or monthly_spending.empty:
        print("No transactions recorded.\n")
        return
    for month in monthly_spending['YearMonth'].unique():
        print(f"{month}:")
        month_data = monthly_spending[monthly_spending['YearMonth'] == month]
        for _, row in month_data.iterrows():
            print(f"  {row['Category']}: {row['Amount']:.2f}")
        print()
