import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file (modify the file path if needed)
data = pd.read_csv('USD_LKR.csv', parse_dates=['Date'], dayfirst=True)

# Convert 'Price' column to numeric, ignoring errors for empty values
data['Price'] = pd.to_numeric(data['Price'], errors='coerce')

# Drop any rows with missing prices
data.dropna(subset=['Price'], inplace=True)

# Sort data by Date
data.sort_values('Date', inplace=True)

# Calculate daily log returns based on 'Price'
data['Log_Returns'] = np.log(data['Price'] / data['Price'].shift(1))

# Parameters for Monte Carlo Simulation
num_simulations = 1000  # Number of simulation paths
num_days = 252  # Number of days to simulate (e.g., 1 year of trading days)
last_price = data['Price'].iloc[-1]  # Start with the last known price
mean = data['Log_Returns'].mean()  # Mean of log returns
std_dev = data['Log_Returns'].std()  # Standard deviation of log returns

# Simulate future price paths
simulation_df = pd.DataFrame()

for sim in range(num_simulations):
    price_series = [last_price]
    for day in range(num_days):
        price = price_series[-1] * np.exp(np.random.normal(mean, std_dev))
        price_series.append(price)
    simulation_df[sim] = price_series

# Plotting the simulation results
plt.figure(figsize=(10, 6))
plt.plot(simulation_df)
plt.title('Monte Carlo Simulation of USD/LKR Exchange Rate From Sep - 2024')
plt.xlabel('Days')
plt.ylabel('USD to LKR Exchange Rate')
plt.grid(True)
plt.savefig('USD_LKR_SIMULATION', dpi=300)