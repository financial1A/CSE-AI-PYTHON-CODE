import pandas as pd

# Load CSV file into a DataFrame
csv_file_path = 'data.csv'  # Replace with your CSV file path
df = pd.read_csv(csv_file_path)

# Specify the row index you want to access
row_index = 3  # For example, let's access the 4th row (indexing starts from 0)

# Use iloc to access the row at row_index
row_data = df.iloc[row_index, :]  # ':' means select all columns for the given row

# Print the data in that row
print(f"\nData in row {row_index}:")
print(row_data)
