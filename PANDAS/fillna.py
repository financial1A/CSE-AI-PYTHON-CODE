import pandas as pd

# Step 1: Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Step 2: Replace all missing values (NaN) with a specific value, like 0
df_filled = df.fillna(0)

# Optional Step 3: Save the updated DataFrame to a new CSV file
df_filled.to_csv('data_filled.csv', index=False)

# Print the modified DataFrame to see the result
print(df_filled)
