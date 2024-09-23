import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV data 
cars = pd.read_csv('CARS.csv')
cins = pd.read_csv('CINSt.csv')
dimo = pd.read_csv('DIMO.csv')

# Clean the 'Change %' column by removing '%' and converting to float
def clean_data(df):
    df['Change %'] = df['Change %'].str.replace('%', '').astype(float)
    df['Vol.'] = df['Vol.'].str.replace('M', 'e6').str.replace('K', 'e3').astype(float)
    return df

cars = clean_data(cars)
cins = clean_data(cins)
dimo = clean_data(dimo)


# carsine datasets based on 'Date' column
merged = cars.merge(cins, on='Date', suffixes=('_cars', '_cins'))
merged = merged.merge(dimo, on='Date', suffixes=('', '_dimo'))

# Calculate correlation between the 'Price' columns
correlation = merged[['Price_cars', 'Price_cins', 'Price']].corr()

print("\nCorrelation Matrix:\n", correlation)

# Scatter plot for visualizing relationships between prices
plt.figure(figsize=(10, 6))

# Plot cars prices in blue
plt.scatter(merged['Price_cars'], merged['Price'], color='blue', label='cars vs dimo')

# Plot cins prices in orange
plt.scatter(merged['Price_cins'], merged['Price'], color='orange', label='cins vs dimo')

plt.title('Scatter Plot: cars vs dimo and cins vs dimo Prices')
plt.xlabel('Prices (cars and cins)')
plt.ylabel('Prices (dimo)')
plt.legend()
plt.savefig('Relationship_prices.png')

# You can also plot correlation heatmap for better visualization
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title('Correlation Heatmap')
plt.savefig('heatmap.png')


# Plotting the prices in the same line chart
plt.figure(figsize=(10, 6))

# Plot cars prices
plt.plot(merged['Date'], merged['Price_cars'], color='blue', label='cars')

# Plot cins prices
plt.plot(merged['Date'], merged['Price_cins'], color='orange', label='cins')

# Plot dimo prices
plt.plot(merged['Date'], merged['Price'], color='green', label='dimo')

# Adding titles and labels
plt.title('Price Trends for cars, cins, and dimo')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()

# Display the plot
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout for clarity
plt.savefig('historical_data.png')