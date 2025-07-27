import pandas as pd
import numpy as np


# Load random data into df
# Define the start and end dates for the index
start_date = "2025-01-01"
end_date = "2025-01-07 23:00:00"

# Generate a DatetimeIndex with hourly frequency
date_index = pd.date_range(start=start_date, end=end_date, freq='H')

# Create a DataFrame with random 'price' values
df = pd.DataFrame({
    'price': np.random.rand(len(date_index)) * 100  # random prices between 0 and 100
}, index=date_index)

# Optionally, display the DataFrame
print(type(date_index))
print(df.head())
print(df.index)  # Confirm that the index is of datetime type and hourly resolution
