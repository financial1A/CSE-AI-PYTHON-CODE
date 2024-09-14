import pandas as pd

# Read the CSV file
df = pd.read_csv('SAMP.csv')

# Convert the "Date" column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

# Extract the day of the week from the Date column (0=Monday, 6=Sunday)
df['DayOfWeek'] = df['Date'].dt.day_name()

# Calculate the price fluctuation (High - Low)
df['Fluctuation'] = df['High'] - df['Low']

# Group by day of the week and calculate the average fluctuation for each day
fluctuation_by_day = df.groupby('DayOfWeek')['Fluctuation'].mean()

# Sort the fluctuation values in descending order
fluctuation_by_day_sorted = fluctuation_by_day.sort_values(ascending=False)

# Output the result
print(fluctuation_by_day_sorted)
