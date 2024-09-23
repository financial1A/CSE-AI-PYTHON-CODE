import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Fetch historical data for crude oil and gold
crude_oil = yf.download('CL=F', start='2015-01-01', end='2023-12-31')
gold = yf.download('GC=F', start='2015-01-01', end='2023-12-31')

# Create a figure and a set of subplots
fig, ax1 = plt.subplots(figsize=(14, 7))

# Plot crude oil prices on the first y-axis
ax1.plot(crude_oil['Close'], color='tab:blue', label='Crude Oil')
ax1.set_xlabel('Date')
ax1.set_ylabel('Crude Oil Price', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Create a second y-axis for gold prices
ax2 = ax1.twinx()
ax2.plot(gold['Close'], color='tab:orange', label='Gold')
ax2.set_ylabel('Gold Price', color='tab:orange')
ax2.tick_params(axis='y', labelcolor='tab:orange')

# Add a title and save the plot
plt.title('Crude Oil and Gold Prices')
fig.tight_layout()
plt.savefig('Historical_price.png')
plt.show()

# Calculate and print the year-by-year correlation
years = pd.date_range(start='2015', end='2024', freq='Y').year
correlations = {}

for year in years:
    crude_oil_year = crude_oil[crude_oil.index.year == year]['Close']
    gold_year = gold[gold.index.year == year]['Close']
    correlation = crude_oil_year.corr(gold_year)
    correlations[year] = correlation
    print(f'The correlation between Crude Oil and Gold prices in {year} is: {correlation}')

# Plot and save the year-by-year correlation
plt.figure(figsize=(10, 5))
plt.plot(list(correlations.keys()), list(correlations.values()), marker='o')
plt.title('Year-by-Year Correlation between Crude Oil and Gold Prices')
plt.xlabel('Year')
plt.ylabel('Correlation')
plt.grid(True)
plt.savefig('Corre.png')
plt.show()
