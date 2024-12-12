import matplotlib.pyplot as plt


def plot_monthly_spending_over_time(df):
    df['YearMonth'] = df['Date'].dt.to_period('M')
    monthly_spending = df.groupby('YearMonth')['Amount'].sum()

    if monthly_spending.empty:
        print("No data to plot.")
        return

    plt.figure(figsize=(10, 6))
    monthly_spending.plot(kind='line', marker='o', color='blue', linestyle='-', linewidth=2)
    plt.title("Monthly Spending Trend", fontsize=16)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Total Spending", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(alpha=0.5)
    plt.tight_layout()
    plt.show()
