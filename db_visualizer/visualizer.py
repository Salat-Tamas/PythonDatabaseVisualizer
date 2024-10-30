import matplotlib.pyplot as plt
import pandas as pd

class Visualizer:
    def __init__(self):
        """Initialize the Visualizer class."""
        plt.style.use('ggplot')  # Using a built-in Matplotlib style

    def plot_data(self, df, x_column, y_column, plot_type='line'):
        """Visualize the data from a DataFrame."""
        
        # Check if the specified columns exist
        if x_column not in df.columns or y_column not in df.columns:
            print("Error: Columns not found in DataFrame.")
            return
        
        # Check the data types of the columns
        x_is_categorical = pd.api.types.is_categorical_dtype(df[x_column]) or pd.api.types.is_object_dtype(df[x_column])
        y_is_categorical = pd.api.types.is_categorical_dtype(df[y_column]) or pd.api.types.is_object_dtype(df[y_column])
        
        # For categorical y_column, convert to category type
        if y_is_categorical:
            df[y_column] = df[y_column].astype('category')
            y_ticks = df[y_column].cat.categories
            y_values = df[y_column].cat.codes  # Numerical representation of categories
        else:
            y_ticks = None  # No custom ticks if y_column is not categorical
            y_values = df[y_column]

        plt.figure(figsize=(10, 6))

        if plot_type == 'line':
            plt.plot(df[x_column], y_values)
        elif plot_type == 'bar':
            plt.bar(df[x_column], y_values)
            plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
        elif plot_type == 'scatter':
            plt.scatter(df[x_column], y_values)

        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title(f"{plot_type.capitalize()} Plot of {y_column} vs {x_column}")
        
        # Set dynamic limits for the y-axis based on data type
        if not y_is_categorical:
            plt.ylim(bottom=0)  # Start y-axis from 0 for numerical data
            plt.yticks(rotation=45)  # Optional: Rotate y-ticks for better visibility
        else:
            if y_ticks is not None:
                plt.yticks(ticks=range(len(y_ticks)), labels=y_ticks)

        plt.tight_layout()  # Adjust layout to prevent clipping of labels
        plt.show()
