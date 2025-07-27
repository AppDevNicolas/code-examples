import pandas as pd
import numpy as np

def ma_calculation_df(df):
    # Moving average calculations
    df['MA_25'] = df['price'].rolling(window=25).mean()
    df['EMA_35'] = df['price'].ewm(span=35, adjust=False).mean()

    return df


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

# print(type(date_index))
# print("df index : ",df.index)  # Confirm that the index is of datetime type and hourly resolution
# Temporarily show all rows/columns
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print("df : ",df)

df = ma_calculation_df(df)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print("df with ma : ",df)