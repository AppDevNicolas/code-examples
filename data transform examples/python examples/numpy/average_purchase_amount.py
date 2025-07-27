import numpy as np

# Generate a 1D array of 1000 random numbers, 
# each representing a simulated transaction amount, 
# drawn from a uniform distribution between 5 and 500
transactions = np.random.uniform(5, 500, size=1000)

# Generate a 1D of 1000 random integers between 0 and 99, 
# each representing a customer ID for the corresponding transaction
customer_ids = np.random.randint(0, 100, size=1000)

# Calculate the total amount spent by each customer:
# - Sum up the transaction amounts by customer ID 
# using the np.bincount function with weights=transactions
# - Output is an array of length 100 (max(customer_ids)+1), where 
# each entry is sum of all transaction amounts for a given customer
total_spent = np.bincount(customer_ids, weights=transactions)
# Count number of transactions for each customer:
# Return an array of length 100, where each entry is the number of times 
# that customer appears (i.e., their number of purchases)    
num_purchases = np.bincount(customer_ids)

# Compute average purchase per customer
avg_purchase = total_spent / num_purchases

print("Average purchase per customer:\n", avg_purchase)
