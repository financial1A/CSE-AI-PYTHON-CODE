import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
file_path = r'C:\Users\Nuwan nsw\Documents\python\ASPI\CSE-AI-PYTHON-CODE\SIMULATION\combined_prices.csv'
df = pd.read_csv(file_path)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Compute the correlation matrix
correlation_matrix = df.corr()

# Create a heatmap of the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix')
plt.tight_layout()

# Save the heatmap as a PNG file
heatmap_path = r'C:\Users\Nuwan nsw\Documents\python\ASPI\CSE-AI-PYTHON-CODE\SIMULATION\correlation_matrix.png'
plt.savefig(heatmap_path, format='png')
plt.close()
