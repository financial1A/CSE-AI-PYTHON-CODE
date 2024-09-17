import pandas as pd

# Specify the path to your CSV file
filename = 'ASPI.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(filename)

# Display the first few rows of the DataFrame
print(df.head())