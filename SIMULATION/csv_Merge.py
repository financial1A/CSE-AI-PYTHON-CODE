import pandas as pd
import os

# Define the directory containing the CSV files
input_directory = r'C:\Users\Nuwan nsw\Documents\python\ASPI\CSE-AI-PYTHON-CODE\SIMULATION'
output_directory = r'C:\Users\Nuwan nsw\Documents\python\ASPI\CSE-AI-PYTHON-CODE\SIMULATION\CSV'

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Initialize a list to hold dataframes for combined CSV
combined_data = []

# Loop through all files in the directory
for filename in os.listdir(input_directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(input_directory, filename)
        
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Extract relevant columns
        df_filtered = df[['Date', 'Price']].copy()  # Make a copy to avoid SettingWithCopyWarning
        
        source_file = filename.split()[0]
        
        # Add source file information
        df_filtered['Source File'] = source_file
        
        # Save each file's filtered data to new CSV in the output directory
        output_file_path = os.path.join(output_directory, f'{os.path.splitext(filename)[0]}_prices.csv')
        df_filtered.to_csv(output_file_path, index=False)
        
        # Add to combined data list
        combined_data.append(df_filtered)

# Concatenate all dataframes into a single dataframe
combined_df = pd.concat(combined_data, ignore_index=True)

# Pivot the dataframe to have prices from different files in separate columns
pivoted_df = combined_df.pivot_table(index='Date', columns='Source File', values='Price', aggfunc='mean').reset_index()

# Save the combined dataframe to a new CSV file
combined_file_path = os.path.join(input_directory, 'combined_prices.csv')
pivoted_df.to_csv(combined_file_path, index=False)

print(f"Combined CSV file saved to: {combined_file_path}")
print(f"Filtered individual CSV files saved to: {output_directory}")
