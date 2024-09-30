import pandas as pd

# Load CSV into a DataFrame
df = pd.read_csv('data.csv')

# Display DataFrame information
df.info()

# Display the shape of the DataFrame
print("Shape of the DataFrame:", df.shape)