def generate_wallet_report(df, filename="wallet_history_report.csv"):
    if df.empty:
        print("No data to save.")
        return

    df_sorted = df.sort_values(by="timestamp")
    df_sorted.to_csv(filename, index=False)

    print(f"Wallet history report saved as {filename}")
