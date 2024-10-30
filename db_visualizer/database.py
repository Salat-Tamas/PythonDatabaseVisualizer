import sqlite3
import pandas as pd

class Database:
    def __init__(self, db_file):
        """Initialize the connection to the SQLite database."""
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file)
    
    def fetch_data(self, query):
        """Run a query and return a DataFrame with the results."""
        try:
            df = pd.read_sql_query(query, self.conn)
            return df
        except Exception as e:
            print(f"Error executing query: {e}")
            return None

    def get_tables(self):
        """Retrieve all tables from the SQLite database."""
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        tables = self.fetch_data(query)
        return tables['name'].tolist() if tables is not None else []

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
