import pandas as pd
import numpy as np


def get_nearest_future_matches(df1, df2):
    """
    Merge df1 with the first future matching records from df2.

    Parameters:
    - df1: First DataFrame with datetime index
    - df2: Second DataFrame with datetime index

    Returns:
    - Merged DataFrame containing original df1 columns plus first future matches from df2
    """
    # Conversion to datetime for operations like merging
    df1.index = pd.to_datetime(df1.index)
    df2.index = pd.to_datetime(df2.index)

    # Ensure dataframes are sorted by index
    df1_sorted = df1.sort_index()
    df2_sorted = df2.sort_index()

    # Perform merge_asof looking forward in time
    merged_df = pd.merge_asof(
        df1_sorted,
        df2_sorted,
        left_index=True,
        right_index=True,
        direction='forward',
        allow_exact_matches=False,
        suffixes=('_df1', '_df2')
    )

    # Convert back to original string format
    merged_df.index = merged_df.index.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    
    # Keep only  rows where 'zero_crossing_close' has a value (is not NaN)
    filtered_df = merged_df[merged_df['price_df2'].notna()]

    return filtered_df


# Load 2 dataframes to test function get_nearest_future_matches
# Generate test data for df1 and df2
np.random.seed(0)

# Create a range of timestamps for both DataFrames
time_index1 = pd.date_range("2025-07-18 09:00", periods=5, freq="5T")
#time_index2 = pd.date_range("2025-07-18 09:02", periods=5, freq="7T")
time_index2 = pd.date_range("2025-07-18 09:02", periods=7, freq="3T")

# Create prices for each DataFrame
prices1 = np.random.uniform(100, 110, len(time_index1))
prices2 = np.random.uniform(200, 210, len(time_index2))

# Construct the DataFrames with timestamp index and a price column
df1 = pd.DataFrame({'price': prices1}, index=time_index1)
df2 = pd.DataFrame({'price': prices2}, index=time_index2)

print("df1:")
print(df1)
print("\ndf2:")
print(df2)

df_result=get_nearest_future_matches(df1, df2)
print(df_result)


