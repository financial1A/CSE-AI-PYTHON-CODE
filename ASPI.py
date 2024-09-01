import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Load the dataset
data = pd.read_csv('CSEASPI.csv')

# Convert 'Date' to datetime and sort by date
data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')
data = data.sort_values('Date')

# Fill missing values (you might want to use a more sophisticated method)
data = data.fillna(method='ffill')

# Feature engineering: Extracting numerical features from the date
data['Day'] = data['Date'].dt.day
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year

# Convert Price to numeric (remove commas and convert to float)
data['Price'] = data['Price'].str.replace(',', '').astype(float)

# Define features and target variable
features = ['Day', 'Month', 'Year']
target = 'Price'

X = data[features]
y = data[target]

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Create future dates
future_dates = [data['Date'].max() + timedelta(days=x) for x in range(1, 181)]  # Next 60 days

# Convert future dates to DataFrame
future_df = pd.DataFrame(future_dates, columns=['Date'])
future_df['Day'] = future_df['Date'].dt.day
future_df['Month'] = future_df['Date'].dt.month
future_df['Year'] = future_df['Date'].dt.year

# Predict future prices
future_features = future_df[features]
future_prices = model.predict(future_features)

# Add random noise to the predictions
np.random.seed(42)  # For reproducibility
noise = np.random.normal(loc=0, scale=0.08 * np.mean(future_prices), size=future_prices.shape)  # Adjust scale to increase noise
future_prices_with_noise = future_prices + noise

# Combine dates with predicted prices
future_df['Predicted Price'] = future_prices_with_noise

# Plot the actual prices and predicted prices with noise
plt.figure(figsize=(14, 7))
plt.plot(data['Date'], data['Price'], color='blue', label='Actual Price')
plt.plot(future_df['Date'], future_df['Predicted Price'], color='orange', linestyle='--', label='Predicted Price with Noise')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Actual vs Predicted Prices (with Noise)')
plt.legend()
plt.grid(True)
plt.show()

# Save future predictions to CSV
future_df.to_csv('Future_Predicted_Prices_With_Noise.csv', index=False)

print('Future prices with random noise predicted and saved to Future_Predicted_Prices_With_Noise.csv')
