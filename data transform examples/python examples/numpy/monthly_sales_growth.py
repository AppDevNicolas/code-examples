import numpy as np
import pandas as pd

store_names = ['A', 'B', 'C', 'D']

# Random daily sales data for 4 stores over 90 days (~3 months).
# Create a 2D NumPy array with shape (4, 90) 
# (i.e., 4 rows and 90 columns)
sales = np.random.randint(100, 500, size=(4, 90))
print("Sales:\n", sales)

# Reshape sales into months: 4 stores, 3 months, 30 days each
# .reshape(4, 3, 30) changes the shape of the sales array so 
# that it becomes a 3D array:
# 4 "rows" (stores) / 3 "months" per row 
# (since 90 days ÷ 3 months = 30 days per month) /
# 30 days per month
monthly_sales = sales.reshape(4, 3, 30)
print("Monthly Sales:\n", monthly_sales)

# Sum daily sales per month
monthly_sales = monthly_sales.sum(axis=2)
print("Monthly Sales per month:\n", monthly_sales)  

# Calculate % growth month-over-month (axis=1)
growth = (monthly_sales[:, 1:] - monthly_sales[:, :-1]) / monthly_sales[:, :-1] * 100
print("Monthly Growth (%):\n", growth)

# Growth rate for each store with its name
for i, name in enumerate(store_names):
    print(f"Store {name} growth: {growth[i]}")

# Create a DataFrame for growth values
growth_df = pd.DataFrame(data=growth, index=store_names, columns=['Month2_vs_Month1', 'Month3_vs_Month2'])
print(growth_df)
