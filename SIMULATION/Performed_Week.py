import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error

# Load the data from CSV
df = pd.read_csv('CFIN.csv')

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

# Extract year, month, and week number within the month
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

# Calculate week number within the month
df['Week_of_Month'] = (df['Day'] - 1) // 7 + 1

# Convert percentage change to numeric
df['Change %'] = df['Change %'].str.replace('%', '').astype(float)

# Prepare features and target
features = df[['Year', 'Month', 'Week_of_Month']]
target = df['Change %']

# Standardize features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(features_scaled, target, test_size=0.2, random_state=42)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict performance
y_pred = model.predict(features_scaled)

# Add predictions to the dataframe
df['Predicted Change %'] = y_pred

# Calculate weekly performance metrics
weekly_performance = df.groupby(['Year', 'Month', 'Week_of_Month']).agg(
    avg_price=('Price', 'mean'),
    avg_change=('Predicted Change %', 'mean')
).reset_index()

# Determine the best performing week in each month
best_weeks = weekly_performance.loc[weekly_performance.groupby(['Year', 'Month'])['avg_change'].idxmax()]

# Print results
print("Best performing week in each month:")
print(best_weeks)

# Save the results to a CSV file
best_weeks.to_csv('best_performing_weeks_sklearn.csv', index=False)
