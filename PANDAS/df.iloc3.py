import pandas as pd

# Read the CSV into a DataFrameR
df = pd.read_csv('data.csv')

# Display the DataFrame
print("Full DataFrame:")
print(df)

# Slice rows and columns using iloc (e.g., from row index 0 to 3, and column index 0 to 3)
start_index = 0
end_index = 3
sliced_df = df.iloc[start_index:end_index, start_index:end_index]

# Display the sliced DataFrame
print("\nSliced DataFrame (from index 0 to 3 for both rows and columns):")
print(sliced_df)
