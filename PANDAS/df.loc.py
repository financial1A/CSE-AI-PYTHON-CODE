import pandas as pd

# Read CSV file into a DataFrame
df = pd.read_csv('data.csv', index_col='id')

# Display the DataFrame
print("DataFrame:")
print(df)

# 1. Select the row with label 1 (row with id=1)
row_1 = df.loc[1]
print("\nRow with id=1:")
print(row_1)

# 2. Select a specific cell (age of id=2)
age_id_2 = df.loc[2, 'age']
print("\nAge of person with id=2:")
print(age_id_2)

# 3. Select multiple rows (id=1, id=3) and columns (name, city)
subset = df.loc[[1, 3], ['name', 'city']]
print("\nSubset with ids 1 and 3 (name, city):")
print(subset)

# 4. Select all rows for a specific column (city)
cities = df.loc[:, 'city']
print("\nAll cities:")
print(cities)
