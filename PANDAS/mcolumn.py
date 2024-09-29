import pandas as pd

# Read the CSV into a DataFrame
df = pd.read_csv('data.csv')

# Select and return only the 'name' and 'age' columns as a new DataFrame
new_df = df[['name', 'age']]

# Display the new DataFrame
print(new_df)