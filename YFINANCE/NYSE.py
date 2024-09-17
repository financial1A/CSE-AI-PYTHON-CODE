import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

# Define the tickers for BTC-USD and GOLD
btc_ticker = 'BTC-USD'
gold_ticker = 'GC=F'  # Gold futures
nyse_ticker = '^NYA'  # NYSE Composite Index

# Download historical data from yfinance
btc_data = yf.download(btc_ticker, start='2024-01-01', end='2024-08-31')
gold_data = yf.download(gold_ticker, start='2024-01-01', end='2024-08-31')
nyse_data = yf.download(nyse_ticker, start='2024-01-01', end='2024-08-31')

# Merge the dataframes based on Date
data = pd.DataFrame({
    'Date': btc_data.index,
    'PriceBTC': btc_data['Adj Close'],
    'PriceGOLD': gold_data['Adj Close'],
    'PriceNYSE': nyse_data['Adj Close']
})

# Drop rows with NaN values
data.dropna(subset=['PriceBTC', 'PriceGOLD', 'PriceNYSE'], inplace=True)

# Calculate the correlation matrix
correlation_matrix = data[['PriceBTC', 'PriceGOLD', 'PriceNYSE']].corr()

# Extract specific correlations
btc_gold_correlation = correlation_matrix.loc['PriceBTC', 'PriceGOLD']

# Other statistics
statistics = data[['PriceBTC', 'PriceGOLD', 'PriceNYSE']].describe()

print("Correlation between PriceBTC and PriceGOLD:", btc_gold_correlation)
print("\nCorrelation Matrix:\n", correlation_matrix)
print("\nDescriptive Statistics:\n", statistics)

# Plot the data
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot PriceBTC
color = 'tab:blue'
ax1.set_xlabel('Date')
ax1.set_ylabel('PriceBTC', color=color)
ax1.plot(data['Date'], data['PriceBTC'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Create a second y-axis for the price of Gold
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('PriceGOLD', color=color)
ax2.plot(data['Date'], data['PriceGOLD'], color=color)
ax2.tick_params(axis='y', labelcolor=color)

# Add legends
fig.tight_layout()
fig.legend(['PriceBTC', 'PriceGOLD'], loc="upper left", bbox_to_anchor=(0.1, 0.9))

plt.title('Prices of BTC and GOLD')
plt.savefig('BTC_GOLD', dpi=300)