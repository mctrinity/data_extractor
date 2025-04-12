import sqlite3


def export_to_sqlite(df, db_path, table_name="data"):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    print(f"Data exported to SQLite database: {db_path} (table: {table_name})")
