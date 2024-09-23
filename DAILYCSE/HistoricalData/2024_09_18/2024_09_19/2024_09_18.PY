import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV data 
comb = pd.read_csv('COMB.csv')
hmb = pd.read_csv('HNB.csv')
samp = pd.read_csv('SAMP.csv')

# Clean the 'Change %' column by removing '%' and converting to float
def clean_data(df):
    df['Change %'] = df['Change %'].str.replace('%', '').astype(float)
    df['Vol.'] = df['Vol.'].str.replace('M', 'e6').str.replace('K', 'e3').astype(float)
    return df

comb = clean_data(comb)
hmb = clean_data(hmb)
samp = clean_data(samp)


# Combine datasets based on 'Date' column
merged = comb.merge(hmb, on='Date', suffixes=('_comb', '_hmb'))
merged = merged.merge(samp, on='Date', suffixes=('', '_samp'))

# Calculate correlation between the 'Price' columns
correlation = merged[['Price_comb', 'Price_hmb', 'Price']].corr()

print("\nCorrelation Matrix:\n", correlation)

# Scatter plot for visualizing relationships between prices
plt.figure(figsize=(10, 6))

# Plot COMB prices in blue
plt.scatter(merged['Price_comb'], merged['Price'], color='blue', label='COMB vs SAMP')

# Plot HMB prices in orange
plt.scatter(merged['Price_hmb'], merged['Price'], color='orange', label='HMB vs SAMP')

plt.title('Scatter Plot: COMB vs SAMP and HMB vs SAMP Prices')
plt.xlabel('Prices (COMB and HMB)')
plt.ylabel('Prices (SAMP)')
plt.legend()
plt.savefig('Relationship_prices.png')

# You can also plot correlation heatmap for better visualization
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title('Correlation Heatmap')
plt.savefig('heatmap.png')


# Plotting the prices in the same line chart
plt.figure(figsize=(10, 6))

# Plot COMB prices
plt.plot(merged['Date'], merged['Price_comb'], color='blue', label='COMB')

# Plot HMB prices
plt.plot(merged['Date'], merged['Price_hmb'], color='orange', label='HMB')

# Plot SAMP prices
plt.plot(merged['Date'], merged['Price'], color='green', label='SAMP')

# Adding titles and labels
plt.title('Price Trends for COMB, HMB, and SAMP')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()

# Display the plot
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout for clarity
plt.savefig('historical_data.png')