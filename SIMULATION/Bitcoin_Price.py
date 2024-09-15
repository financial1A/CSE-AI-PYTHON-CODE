import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Fetch Bitcoin data from yfinance (last 1 year)
btc_data = yf.download('BTC-USD', period='1y')

# Reset index to get 'Date' as a column
btc_data.reset_index(inplace=True)

# Convert Date to ordinal format for regression (e.g., number of days since 1970-01-01)
btc_data['Date_ordinal'] = btc_data['Date'].map(pd.Timestamp.toordinal)

# Define features (X) and target (y) for regression
X = btc_data[['Date_ordinal']]
y = btc_data['Close']

# Standardize the date feature
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the prices using the trained model
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Plot the actual prices and predicted regression line
plt.figure(figsize=(12, 6))
plt.plot(btc_data['Date'], btc_data['Close'], label='Actual BTC Price', color='blue')
plt.plot(btc_data['Date'], model.predict(X_scaled), label='Linear Regression Line', color='red')

plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('Bitcoin Price with Linear Regression Prediction')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('btc_linear_regression.png')
plt.close()

print("Linear regression model trained and plot saved as 'btc_linear_regression.png'")

# --- Monte Carlo Simulation for Next 1 Year of Prices ---

# Calculate daily returns
btc_data['Returns'] = btc_data['Close'].pct_change()

# Parameters for Monte Carlo simulation
last_price = btc_data['Close'].iloc[-1]
num_simulations = 1000
num_days = 365

# Calculate the mean and standard deviation of returns
mean_return = btc_data['Returns'].mean()
std_dev = btc_data['Returns'].std()

# Simulate future price paths
simulated_prices = np.zeros((num_days, num_simulations))

for i in range(num_simulations):
    # Initialize the first day price
    simulated_prices[0, i] = last_price
    
    # Generate simulated price path
    for t in range(1, num_days):
        random_shock = np.random.normal(loc=mean_return, scale=std_dev)
        simulated_prices[t, i] = simulated_prices[t-1, i] * (1 + random_shock)

# Generate date range for the next year
simulated_dates = pd.date_range(btc_data['Date'].max() + pd.Timedelta(days=1), periods=num_days)

# Plot the Monte Carlo simulations
plt.figure(figsize=(12, 6))

# Plot multiple simulated paths
for i in range(num_simulations):
    plt.plot(simulated_dates, simulated_prices[:, i], color='green', alpha=0.1)

plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title(f'Simulated Bitcoin Prices for the Next Year ({num_simulations} Simulations)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the simulation plot
plt.savefig('btc_montecarlo_simulation.png')
plt.close()

print(f"Simulated Bitcoin prices for the next year using Monte Carlo method saved as 'btc_montecarlo_simulation.png'")
