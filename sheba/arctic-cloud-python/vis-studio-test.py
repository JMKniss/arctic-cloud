"""
Recalibrating the Brunt equation using SHEBA data

Jason Kniss
Feb 02 2024

This script is used to process the unfiltered code, intended as a test of
functionality and for the author to practice python coding

"""

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
from matplotlib.ticker import MaxNLocator

# Load data
tower_hrly = 'main_file6_hd.txt' # This will need to be updated to relative path
df = pd.read_csv(tower_hrly, delimiter='\t')

# Replace flagged data with NaN
df.replace({9999: pd.NA, 999: pd.NA}, inplace=True)

# Display the first few rows of the DataFrame
print(df.head())

# Calculate effective emissivity
sigma = 5.67e-8

df['T2.5_K'] = df['T2.5'] + 273.15 # Convert temperature from Celsius to Kelvin
df['T10_K'] = df['T10'] + 273.15 # Convert temperature from Celsius to Kelvin

df['eps2.5'] = df['LWd'] / (sigma * df['T2.5_K']**4)
df['eps10'] = df['LWd'] / (sigma * df['T10_K']**4)

# Create a mask to filter out NaN values
mask2 = df['eps2.5'].notna()
mask10 = df['eps10'].notna()

# Convert Julian days to datetime
df['time'] = pd.to_datetime((df['JD']+2450449.5), origin='julian', unit='D')

# Plot e_sky over time
plt.scatter(df['time'][mask2], df['eps2.5'][mask2], label='2.5m', s=0.5, color='blue')
plt.scatter(df['time'][mask10], df['eps10'][mask10], label='10m', s=0.5, color='red')
plt.xlabel('Time')
plt.ylabel('Emissivity')
plt.title('Emissivity over Time')
plt.legend()
plt.grid(True)

## Set ticks at regular intervals

# Find the start and end dates in your DataFrame
start_date = df['time'].min()
end_date = df['time'].max()

# Generate ticks at regular intervals between start and end dates
ticks = pd.date_range(start=start_date, end=end_date, freq='42D')
tick_labels = [date.strftime('%Y-%m-%d') if i % 4 == 0 else None for i, date in enumerate(ticks)]

plt.xticks(ticks, tick_labels)

plt.show()



