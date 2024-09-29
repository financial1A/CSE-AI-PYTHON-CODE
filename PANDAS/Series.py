import pandas as pd

# Create a pandas Series
s = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

# Select the item at the second position (index 1)
item = s.iloc[1]
1
print("Item selected with iloc[1]:", item)


# Select the item with label 'c'
item = s.loc['c']

print("Item selected with loc['c']:", item)
