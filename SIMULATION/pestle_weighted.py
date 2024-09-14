import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load historical stock data
data = pd.read_csv('SAMP.csv', index_col='Date', parse_dates=True)

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
start_date = data.index[0]  # Use the last date from the dataset as the start date
future_dates = pd.date_range(start=start_date, periods=num_days, freq='B')  # 'B' for business days

# Define PESTLE factor weights
pestle_weights = {
    'Political': 0.30,
    'Economic': 0.20,
    'Social': 0.20,
    'Technological': 0.15,
    'Legal': 0.05,
    'Environmental': 0.10
}

# Define noise levels for each PESTLE factor (six different levels)
noise_levels = {
    'High': returns.std() * 1,
    'Medium_High': returns.std() * 2,
    'Medium': returns.std() * 0.5,
    'Medium_Low': returns.std() * 0.5,
    'Low': returns.std() * 0.5,
    'Very_Low': returns.std() * 0.25
}

# Define noise categories for each PESTLE factor
pestle_noise_factors = {
    'Political': 'High',
    'Economic': 'Medium_High',
    'Social': 'Medium',
    'Technological': 'Medium_Low',
    'Legal': 'Low',
    'Environmental': 'Very_Low'
}

def get_noise_level(factor):
    """Return the standard deviation for noise based on factor category."""
    noise_category = pestle_noise_factors.get(factor, 'Medium')
    return noise_levels.get(noise_category, returns.std())

# Initialize an array to store the simulation results
simulated_prices = np.zeros((num_simulations, num_days))

# Perform the Monte Carlo simulation with PESTLE adjustments
for i in range(num_simulations):
    # Start with the last available price
    price = data['Price'].iloc[0]  # Start with the last price from the data
    simulated_prices[i, 0] = price
    
    for j in range(1, num_days):
        # Initialize the day's return
        daily_return = 0
        
        # Add weighted noise for each PESTLE factor
        for factor, weight in pestle_weights.items():
            # Determine the standard deviation of noise using the function
            factor_noise_std = get_noise_level(factor)
            factor_noise = np.random.normal(0, factor_noise_std)
            
            # Apply the factor's impact
            daily_return += weight * factor_noise
        
        # Adjust the price based on the calculated daily return
        price = price * (1 + daily_return)
        simulated_prices[i, j] = price

# Plot the results
plt.figure(figsize=(12, 6))
for i in range(num_simulations):
    plt.plot(future_dates, simulated_prices[i], color='blue', alpha=0.1)
plt.title('Monte Carlo Simulation of Future Stock Prices with PESTLE Factor Effects')
plt.xlabel('Date')
plt.ylabel('Simulated Price')
plt.grid(True)

# Save the plot as a PNG file
plt.savefig('monte_carlo_future_prices_with_pestle_factors.png', dpi=300)

# Analyze the results
final_prices = simulated_prices[:, -1]
mean_final_price = np.mean(final_prices)
percentile_5th = np.percentile(final_prices, 5)
percentile_95th = np.percentile(final_prices, 95)

print(f"Mean final simulated price: {mean_final_price:.2f}")
print(f"5th percentile: {percentile_5th:.2f}")
print(f"95th percentile: {percentile_95th:.2f}")
