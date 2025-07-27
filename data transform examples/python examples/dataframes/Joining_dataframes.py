import pandas as pd

df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Age': [25, 30, 35]})

# Using merge: joins DataFrames based on common column(s)
merged_df = pd.merge(df1, df2, on='ID', how='inner')
print("Merged DataFrame:")
print(merged_df)

# Using join: joins DataFrames based on index (or key), usually with df.join()
df1.set_index('ID', inplace=True)
df2.set_index('ID', inplace=True)
joined_df = df1.join(df2, how='inner')
print("\nJoined DataFrame:")
print(joined_df)

# Using concat: concatenates DataFrames vertically (axis=0) or horizontally (axis=1)
concat_df = pd.concat([df1, df2], axis=1)
print("\nConcatenated DataFrame:")
print(concat_df)
