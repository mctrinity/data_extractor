def export_to_excel(df, filename):
    df.to_excel(filename, index=False)
    print(f"Data exported to Excel: {filename}")
