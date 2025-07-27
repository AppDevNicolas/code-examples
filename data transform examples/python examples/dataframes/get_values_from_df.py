import pandas as pd
import numpy as np

def get_high_score_dt_values(df, high_score_dt):

    price_high_score = df.loc[
        high_score_dt,
        'price'
    ]

    volume_high_score = df.loc[
        high_score_dt,
        'volume'
    ]

    return price_high_score, volume_high_score

def get_1st_values_price_over50(df):
    row = df[df['price'] > 50].iloc[0]
    return row.name, row['price'], row['volume']
	
# Load random data into df
# Define the start and end dates for the index
start_date = "2025-01-01"
end_date = "2025-01-07 23:00:00"

# Generate a DatetimeIndex with hourly frequency
date_index = pd.date_range(start=start_date, end=end_date, freq='H')

# Create a DataFrame with random 'price' values and a column 'volume'
# Assuming date_index is already defined
df = pd.DataFrame({
    'price': np.random.rand(len(date_index)) * 100,
    'volume': np.random.uniform(10, 1000, len(date_index))
}, index=date_index)

df.index.name = 'datetime'

print(type(date_index))
print("df index : ",df.index)  # Confirm that the index is of datetime type and hourly resolution
# Temporarily show all rows/columns
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print("df : ",df)

first_dt = pd.to_datetime("2025-01-07 21:00:00")
print("first_dt : ", first_dt)
price_high_score, volume_high_score = get_high_score_dt_values(df,first_dt)
print("price_high_score : ",price_high_score)
print("volume_high_score : ",volume_high_score)

price_over50_dt, price_over50, price_over50_vol = get_1st_values_price_over50(df)
print("price_over50_dt : ", price_over50_dt)
print("price_over50 : ",price_over50)
print("price_over50_vol : ",price_over50_vol)