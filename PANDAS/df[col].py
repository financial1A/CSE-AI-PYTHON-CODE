import pandas as pd

# Read CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Access the 'name' column
names = df['name']
print("Names column:")
# for i, name in names.items():
# print(name)
print(names)

# Access the 'age' column
ages = df['age']
print("\nAges column:")
print(ages)
