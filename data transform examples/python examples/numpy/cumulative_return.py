import numpy as np

# Simulate daily returns (mean=0.0005, std=0.01).
# Generate a 2D numpy array of shape (252, 5)
# Each element is sampled from a normal (Gaussian) distribution with:
# - Mean (expected daily return) = 0.0005 (or 0.05%)
# - Standard deviation (volatility) = 0.01 (or 1%)
# 252 corresponds to the number of trading days in a year
# 5 different assets or stocks
daily_returns = np.random.normal(0.0005, 0.01, size=(252, 5))
print("daily_returns:\n", daily_returns)

# Calculate cumulative returns per asset:
# - Calculation: 1 + daily_returns converts returns into growth factors. 
#   (example ... daily return is 0.01 (1%) => growth factor = 1.01)
# - np.cumprod(..., axis=0) calculates the cumulative product 
#   of these growth factors along each column (vertically top to bottom). 
#   (It multiplies elements accross the rows for each column...since axis=0)
#   This simulates the compound growth of the investment over time.
#   Subtracting 1 converts cumulative growth factors back into 
#   cumulative returns.
# - cumulative_returns is a (252, 5) array giving  
#   the cumulative (total) return from day 1 to day t for each asset
cumulative_returns = np.cumprod(1 + daily_returns, axis=0) - 1
print("cumulative_returns:\n", cumulative_returns)

# Transpose to get shape (5 assets, 252 days)
# - Transpose the array from shape (252, 5) to (5, 252)
# - Each row now corresponds to an asset
returns_transposed = cumulative_returns.T

print("Cumulative returns for first asset:\n", returns_transposed[0])
