import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load historical stock data 
data = pd.read_csv('HAYL.csv', index_col='Date', parse_dates=True)

# Convert 'Price' column to numeric, coercing errors
data['Price'] = pd.to_numeric(data['Price'], errors='coerce')

# Fill or drop any NaN values after conversion
data = data.ffill().dropna()

# Calculate daily returns using the 'Price' column
returns = data['Price'].pct_change().dropna()

# Set parameters for the Monte Carlo simulation
num_simulations = 100
num_days = 252  # Number of trading days in a year

# Generate future dates starting from the last available date
start_date = pd.to_datetime('09/02/2024')  # Starting date for future simulation
future_dates = pd.date_range(start=start_date, periods=num_days, freq='B')  # 'B' for business days

# Initialize an array to store the simulation results
simulated_prices = np.zeros((num_simulations, num_days))

# Perform the Monte Carlo simulation
for i in range(num_simulations):
    # Start with the last available price
    price = data['Price'].iloc[-1]
    simulated_prices[i, 0] = price
    
    # Simulate the future prices using random normal distribution based on historical mean and std deviation
    for j in range(1, num_days):
        simulated_return = np.random.normal(returns.mean(), returns.std())
        price = price * (1 + simulated_return)
        simulated_prices[i, j] = price

# Plot the results
plt.figure(figsize=(12, 6))
for i in range(num_simulations):
    plt.plot(future_dates, simulated_prices[i], color='blue', alpha=0.1)
plt.title('Monte Carlo Simulation of Future Stock Prices')
plt.xlabel('Date')
plt.ylabel('Simulated Price')

# Save the plot as a PNG file
plt.savefig('monte_carlo_future_prices_100.png', dpi=300)

# Analyze the results
final_prices = simulated_prices[:, -1]
mean_final_price = np.mean(final_prices)
percentile_5th = np.percentile(final_prices, 5)
percentile_95th = np.percentile(final_prices, 95)

print(f"Mean final simulated price: {mean_final_price:.2f}")
print(f"5th percentile: {percentile_5th:.2f}")
print(f"95th percentile: {percentile_95th:.2f}")