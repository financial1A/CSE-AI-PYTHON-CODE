import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Drop rows with any NaN values
df_cleaned = df.dropna()

# Drop columns with any NaN values
df_cleaned_columns = df.dropna(axis=1)

# Drop rows only if all values are NaN
df_cleaned_all = df.dropna(how='all')

# Drop rows with fewer than 3 non-NaN values
df_cleaned_thresh = df.dropna(thresh=3)
