import numpy as np

# Examples of conversion with array a
a = np.array([1, 2, 3])
print(a.shape) 
print(f" a =   {a}" ) 

# Convert it to (n, 1) — a column vector.
a2d_col = a[:, np.newaxis]
print(a2d_col.shape) 
print(f" a2d_col =   {a2d_col}" )

# Convert it to (1, n) — a row vector
a2d_row = a[np.newaxis,:]
print(a2d_row.shape) 
print(f" a2d_row =   {a2d_row}" ) 

# Application stocks: Initial stock per product
init_stock = np.random.randint(200, 500, size=6)
print(f" initial stock = {init_stock}")
print(f" initial stock 2D = {init_stock[:, np.newaxis]}")

consum_prod_month = np.random.randint(10, 70, size=(6, 12))
print(f" consum product by month = {consum_prod_month}")

consum_prod_month_cumsum = np.cumsum(consum_prod_month, axis=1)
print(f" consum product cumsum= {consum_prod_month_cumsum}")

consum_prod_sum = np.sum(consum_prod_month, axis=1)
#print(f" consum_prod_sum= {consum_prod_sum}")

# Remaining stock after each month (cumulative consumption)
remaining_stock = init_stock[:, np.newaxis] -  consum_prod_month_cumsum
print("Remaining stock per month:\n", remaining_stock)

# Identify months where restocking needed (<50 units)
restock_needed = remaining_stock < 50

print("Restocking needed (True=Yes):\n", restock_needed)
