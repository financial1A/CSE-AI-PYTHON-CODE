import pandas as pd

# Load CSV into a DataFrame
df = pd.read_csv('data.csv')

print("\nFirst 2 rows of the DataFrame:")
print(df.head(2))

print("\nLast 2 rows of the DataFrame:")
print(df.tail(2))
