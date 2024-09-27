import pandas as pd

# Load CSV file into a DataFrameRSS
csv_file_path = 'data.csv'  # Replace with your CSV file path
df = pd.read_csv(csv_file_path)

# Specify the row and column indices you want to access
row_index = 2  # For example, let's access the 3rd row (indexing starts from 0)
col_index = 1  # Let's access the 2nd column (indexing starts from 0)R

# Use iloc to access the specific element at (row_index, col_index)
element = df.iloc[row_index, col_index]

# Print the specific element
print(f"\nElement at row {row_index} and column {col_index}: {element}")
