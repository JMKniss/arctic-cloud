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
df.replace({9999: np.nan, 999: np.nan}, inplace=True)

# Display the first few rows of the DataFrame
print(df.head())

'''Effective Emissivity'''
# Calculate effective emissivity from measure DLR and T
sigma = 5.67e-8

df['T2.5_K'] = df['T2.5'] + 273.15 # Convert temperature from Celsius to Kelvin
df['T10_K'] = df['T10'] + 273.15 # Convert temperature from Celsius to Kelvin

df['eps2.5'] = df['LWd'] / (sigma * df['T2.5_K']**4)
df['eps10'] = df['LWd'] / (sigma * df['T10_K']**4)


'''Calculate expected DLR''' # This will probably be changed when we try to fit clear sky data
# Calculate Partial Pressure of water vapor (Pa)
df['Pw2.5'] = ((df['q2.5'] / 1000 * (df['Press'] * 100)) / (df['q2.5'] / 1000 + 0.622))/100
df['Pw10'] = ((df['q10'] / 1000 * (df['Press'] * 100)) / (df['q10'] / 1000 + 0.622))/100


# Calculate clear sky emissivity
df['e2.5'] = (0.618 + 0.054*np.sqrt(df['Pw2.5']))
df['e10'] = (0.618 + 0.054*np.sqrt(df['Pw10']))

# Calculate expected DLR
df['DLR2.5'] = df['e2.5']*sigma*(df['T2.5_K']**4)
df['DLR10'] = df['e10']*sigma*(df['T10_K']**4)


'''Generate Plots'''

# Convert Julian days to datetime
df['time'] = pd.to_datetime((df['JD']+2450449.5), origin='julian', unit='D')

# Create a mask to filter out NaN values
epsmask2 = df['eps2.5'].notna()
epsmask10 = df['eps10'].notna()
DLRmask2 = df['DLR2.5'].notna() & df['LWd'].notna()
DLRmask10 = df['DLR10'].notna() & df['LWd'].notna()

## Plot e_sky over time
plt.scatter(df['time'][epsmask2], df['eps2.5'][epsmask2], label='2.5m', s=0.5, color='blue')
plt.scatter(df['time'][epsmask10], df['eps10'][epsmask10], label='10m', s=0.5, color='red')
plt.xlabel('Time')
plt.ylabel('Emissivity')
plt.title('Emissivity over Time')
plt.legend()
plt.grid(True)

# Set ticks at regular intervals

# Find the start and end dates in your DataFrame
start_date = df['time'].min()
end_date = df['time'].max()

# Generate ticks at regular intervals between start and end dates
ticks = pd.date_range(start=start_date, end=end_date, freq='42D')
tick_labels = [date.strftime('%Y-%m-%d') if i % 4 == 0 else None for i, date in enumerate(ticks)]

plt.xticks(ticks, tick_labels)

plt.show()

## Plot expected DLR vs measured DLR
plt.scatter(df['LWd'][DLRmask2], df['DLR2.5'][DLRmask2], label='2.5m', s=0.5, color='blue')
plt.scatter(df['LWd'][DLRmask10], df['DLR10'][DLRmask10], label='10m', s=0.5, color='red')
plt.xlabel('Measured DLR')
plt.ylabel('Expected DLR')
plt.title('Expected vs Measured DLR')
plt.legend()


# Calculate the maximum value for x and y
max_value = max(np.nanmax(df['LWd'][DLRmask2]), np.nanmax(df['DLR2.5'][DLRmask2]))
plt.xlim(0, max_value)
plt.ylim(0, max_value)
plt.grid(True)
plt.plot([0,max_value],[0,max_value])

plt.show()