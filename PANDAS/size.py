import pandas as pd

# Load CSV into a DataFrame
df = pd.read_csv('data.csv')

# Get the size of the DataFrame
print("\nSize of the DataFrame:", df.size)

# Get the index of the DataFrame
print("\nIndex of the DataFrame:", df.index)

# Get the column labels of the DataFrame
print("\nColumns in the DataFrame:", df.columns)