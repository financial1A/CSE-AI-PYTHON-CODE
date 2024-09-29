import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Check for null values using pd.isnull()
null_values = pd.isnull(df)
print("Is Null:")
print(null_values)

# Check for non-null values using pd.notnull()
not_null_values = pd.notnull(df)
print("\nNot Null:")
print(not_null_values)

print("\n")

# Select rows where 'Age' is missing (NaN)
missing_age = df[pd.isnull(df['Age'])]
print(missing_age)
