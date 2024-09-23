import pandas as pd

# Read CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    name = row.get('name')  # Safely get the 'name' column value
    age = row.get('age')    # Safely get the 'age' column value
    print(f"Name: {name}, Age: {age}")
