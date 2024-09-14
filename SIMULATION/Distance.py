import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

# Load the data from the CSV file
df = pd.read_csv('ASPI.csv')

# Remove commas from numeric values and convert them to floats
df['Price'] = df['Price'].str.replace(',', '').astype(float)
df['High'] = df['High'].str.replace(',', '').astype(float)
df['Low'] = df['Low'].str.replace(',', '').astype(float)

# Convert the "Date" column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

# Sort the data by date just in case
df = df.sort_values(by='Date')

# Find local maxima (peaks) and local minima (troughs)
df['maxima'] = df['Price'][argrelextrema(df['Price'].values, np.greater)[0]]
df['minima'] = df['Price'][argrelextrema(df['Price'].values, np.less)[0]]

# Find the distances between consecutive peaks (local maxima) and troughs (local minima)
# Get the indices of maxima and minima
maxima_indices = df.dropna(subset=['maxima']).index
minima_indices = df.dropna(subset=['minima']).index

# Combine maxima and minima indices, sort them, and compute distances between consecutive extrema
extrema_indices = np.sort(np.concatenate((maxima_indices, minima_indices)))
extrema_dates = df['Date'].iloc[extrema_indices]
distances = np.diff(extrema_dates).astype('timedelta64[D]').astype(int)

# Calculate the average, maximum, and minimum distances
average_distance = np.mean(distances)
max_distance = np.max(distances)
min_distance = np.min(distances)

# Print the average, maximum, and minimum distances
print(f"Average distance between short-term bell shapes: {average_distance} days")
print(f"Maximum distance between short-term bell shapes: {max_distance} days")
print(f"Minimum distance between short-term bell shapes: {min_distance} days")

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Price'], label='Price', color='blue', lw=1.5)

# Plot maxima (peaks) and minima (troughs)
plt.scatter(df['Date'].loc[maxima_indices], df['Price'].loc[maxima_indices], color='green', label='Peaks', marker='^', s=100)
plt.scatter(df['Date'].loc[minima_indices], df['Price'].loc[minima_indices], color='red', label='Troughs', marker='v', s=100)

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('ASPI Price with Short-Term Bell Shapes')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot instead of showing it
plt.savefig('aspi_bell_shapes.png')

# Optional: Close the plot to free up memory if running multiple times
plt.close()
