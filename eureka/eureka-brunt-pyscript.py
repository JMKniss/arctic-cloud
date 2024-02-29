"""
# Arctic-calibrated Brunt equation

## Jason Kniss
## Feb 14 2024

### Calibrate the Brunt equation using data from the Eureka site
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

## Import data from Eureka observatory

towermet_05152011_file = '../notebooks/data/eureka-data/tower-met/eurmeteorologicaltwr.b1.20110515.000000.txt'
# Add additional tower met data files

towerrad_05152011_file = '../notebooks/data/eureka-data/tower-rad/eurradiationtwr.b1.20110515.000000.txt'
# Add additional tower radiation files

### Create meteorological dataframes


#### Extract the header data separately (delimiters are not the same)

with open(towermet_05152011_file, "r") as f:
    lines = f.readlines()

header = lines[0].strip().split()
data_rows = [line.strip().split("\t") for line in lines[1:]]

df1 = pd.DataFrame(data_rows, columns=header)
# Rename the dataframe when more data is imported
 
df1 = df1.astype('float')

### Create radiation dataframes
#### Note* it may be better to just add the radiation column to the tower dataframe in one step

with open(towerrad_05152011_file, "r") as f:
    lines = f.readlines()

header = lines[0].strip().split()
data_rows = [line.strip().split("\t") for line in lines[1:]]

df2 = pd.DataFrame(data_rows, columns=header)
# Rename the dataframe when more data is imported

df2 = df2.astype('float')

#### Concatenate dataframes
df = pd.concat([df1, df2[df2.columns[-5:]]], axis=1)

#### Set time as the index
def julian_to_date(julian_day, base_year=2011):
    base_date = datetime(base_year, 1, 1)
    target_date = base_date + timedelta(days=julian_day - 1)
    return target_date.strftime('%Y-%m-%d')

def hourmin_to_time(hourmin):
    hours = int(hourmin // 100)
    minutes = int(hourmin % 100)
    return f'{hours:02}:{minutes:02}:00'

# Convert Julian Day to date
df['Date'] = df['JulianDay'].apply(julian_to_date)

# Convert HourMin to time
df['Time'] = df['HourMin'].apply(hourmin_to_time)

# Combine date and time into a single datetime column
df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])

# Drop intermediate columns
df.drop(columns=['Date', 'Time'], inplace=True)



 ### 1) Calculate effective emissivity
 
 # Calculate effective emissivity from measured DLR and Temperature
SIGMA = 5.67e-8

df['T2_K'] = df['2MTair[degC]'] + 273.15 # Convert temperature from Celsius to Kelvin
df['T6_K'] = df['6MTair[degC]'] + 273.15 # Convert temperature from Celsius to Kelvin
df['T10_K'] = df['10MTair[degC]'] + 273.15 # Convert temperature from Celsius to Kelvin

df['eps2'] = df['LWTotalDownwelling[W/m^2]'] / (SIGMA * df['T2_K']**4)
df['eps6'] = df['LWTotalDownwelling[W/m^2]'] / (SIGMA * df['T6_K']**4)
df['eps10'] = df['LWTotalDownwelling[W/m^2]'] / (SIGMA * df['T10_K']**4)

### 2) Calculate expected DLR 
#### *This step will come after fitting a power curve to the measured DLR data*

# Calculate Partial Pressure of water vapor (hPa)

df['Pw2'] = 610.94*(df['2MRH[%]']/100)*np.exp((17.625*(df['T2_K'] - 273.15))/(df['T2_K'] - 30.11))/100
df['Pw6'] = 610.94*(df['6MRH[%]']/100)*np.exp((17.625*(df['T6_K'] - 273.15))/(df['T6_K'] - 30.11))/100
df['Pw10'] = 610.94*(df['10MRH[%]']/100)*np.exp((17.625*(df['T10_K'] - 273.15))/(df['T10_K'] - 30.11))/100

#### Calculate theoretical clear sky emissivity

df['e2'] = (0.52 + 0.065*np.sqrt(df['Pw2']))
df['e6'] = (0.52 + 0.065*np.sqrt(df['Pw6']))
df['e10'] = (0.52 + 0.065*np.sqrt(df['Pw10']))

#### Calibrated parameters per Li et al. 2017. **Don't Run both emissivity cells**

# Calculate clear sky emissivity
df['e2'] = (0.618 + 0.054*np.sqrt(df['Pw2']))
df['e6'] = (0.618 + 0.054*np.sqrt(df['Pw6']))
df['e10'] = (0.618 + 0.054*np.sqrt(df['Pw10']))

#### Parameters per the original Brunt equation. **Don't Run both emissivity cells**

# Calculate expected DLR
df['DLR2'] = df['e2']*SIGMA*(df['T2_K']**4)
df['DLR6'] = df['e6']*SIGMA*(df['T6_K']**4)
df['DLR10'] = df['e10']*SIGMA*(df['T10_K']**4)

# Create a mask to filter out NaN values
epsmask2 = df['eps2'].notna()
epsmask6 = df['eps6'].notna()
epsmask10 = df['eps10'].notna()
DLRmask2 = df['DLR2'].notna() & df['LWTotalDownwelling[W/m^2]'].notna()
DLRmask6 = df['DLR6'].notna() & df['LWTotalDownwelling[W/m^2]'].notna()
DLRmask10 = df['DLR10'].notna() & df['LWTotalDownwelling[W/m^2]'].notna()

## Plot e_sky over time
plt.scatter(df.index[epsmask2], df['eps2'][epsmask2], label='2m', s=0.5, color='blue')
# plt.scatter(df.index[epsmask6], df['eps6'][epsmask6], label='6m', s=0.5, color='cyan')
# plt.scatter(df.index[epsmask10], df['eps10'][epsmask10], label='10m', s=0.5, color='red')

# Set ticks at regular intervals
# Find the start and end dates in your DataFrame
# start_date = df.index.min()
# end_date = df.index.max()

# # Generate ticks at regular intervals between start and end dates
# ticks = pd.date_range(start=start_date, end=end_date, freq='4h')
# tick_labels = [date.strftime('%Y-%m-%d') if i % 4 == 0 else None for i, date in enumerate(ticks)]

# Format the plot
plt.ylim(0.68, 0.89)
# plt.xticks(ticks, tick_labels)
plt.xlabel('Time')
plt.ylabel('Emissivity')
plt.title('Emissivity over Time')
plt.legend()
plt.grid()
plt.show()

# Save plot as .png
# plt.savefig('emissivity.png')

## Plot expected DLR vs measured DLR
plt.scatter(df['LWTotalDownwelling[W/m^2]'][DLRmask2], df['DLR2'][DLRmask2], label='2m', s=0.5, color='blue')
# plt.scatter(df['LWTotalDownwelling[W/m^2]'][DLRmask6], df['DLR6'][DLRmask6], label='6m', s=0.5, color='cyan')
# plt.scatter(df['LWTotalDownwelling[W/m^2]'][DLRmask10], df['DLR10'][DLRmask10], label='10m', s=0.5, color='red')

# Calculate the maximum value for x and y
max_value = max(np.nanmax(df['LWTotalDownwelling[W/m^2]'][DLRmask2]), np.nanmax(df['DLR2'][DLRmask2]))
plt.xlim(0, max_value)
plt.ylim(0, max_value)
plt.grid()
plt.plot([0,max_value],[0,max_value])


# Format the plot
plt.xlabel('Measured DLR')
plt.ylabel('Expected DLR')
plt.title('Expected vs Measured DLR')
plt.legend()
plt.show()

# Save plot as .png
# plt.savefig('exp-vs-measured-DLR.png')

## Plot expected DLR vs measured DLR
plt.scatter(df['LWTotalDownwelling[W/m^2]'][DLRmask2], df['DLR2'][DLRmask2], label='2m', s=0.5, color='blue')
# plt.scatter(df['LWTotalDownwelling[W/m^2]'][DLRmask6], df['DLR6'][DLRmask6], label='6m', s=0.5, color='cyan')
# plt.scatter(df['LWTotalDownwelling[W/m^2]'][DLRmask10], df['DLR10'][DLRmask10], label='10m', s=0.5, color='red')

# Calculate the maximum value for x and y
max_value = max(np.nanmax(df['LWTotalDownwelling[W/m^2]'][DLRmask2]), np.nanmax(df['DLR2'][DLRmask2]))
min_value = min(np.nanmin(df['LWTotalDownwelling[W/m^2]'][DLRmask2]), np.nanmin(df['DLR2'][DLRmask2]))
plt.xlim(min_value, max_value)
plt.ylim(min_value, max_value)
plt.grid()
plt.plot([min_value,max_value],[min_value,max_value])

# Format the plot
plt.xlabel('Measured DLR')
plt.ylabel('Expected DLR')
plt.title('Expected vs Measured DLR')
plt.legend()
plt.show()
# Save plot as .png
# plt.savefig('exp-vs-measured-DLR.png')