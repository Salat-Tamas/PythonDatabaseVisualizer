from db_visualizer.database import Database
from db_visualizer.visualizer import Visualizer

def main():
    db_file = "partial.db"
    db = Database(db_file)
    viz = Visualizer()

    try:
        # tables = db.get_tables()
        # print("Available tables:", tables)
        
        # # Example: Visualize data from a specific table
        # table_name = input("Enter the table name to visualize: ")
        # if table_name not in tables:
        #     print("Table not found.")
        #     return

        table_name = "exam_students"

        # Fetch data from the selected table
        df = db.fetch_data(f"SELECT * FROM {table_name}")
        if df is not None:
            print("Data Sample:\n", df.head())

            # Choose columns to visualize
            x_column = input("Enter the column name for x-axis: ")
            y_column = input("Enter the column name for y-axis: ")
            plot_type = input("Enter plot type (line/bar/scatter): ").strip().lower()

            # Plot data
            viz.plot_data(df, x_column, y_column, plot_type)
        else:
            print("No data to display.")
    finally:
        db.close()

if __name__ == "__main__":
    main()
