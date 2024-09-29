import pandas as pd

# Step 1: Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Step 2: Replace all occurrences of 1 with 'one'
df = df.replace('Los Angeles', 'LA')

# Step 4: Print the DataFrame to see the changes
print(df)