def export_to_csv(df, filename):
    df.to_csv(filename, index=False)
    print(f"Data exported to CSV: {filename}")
