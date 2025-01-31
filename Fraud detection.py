from scipy.stats import binom

# Define parameters
n = 1000  # Total transactions
k = 25    # Number of fraudulent transactions
p = 0.02  # Probability of a single transaction being fraudulent

# Calculate binomial probability P(X = 25)
probability = binom.pmf(k, n, p)

# Print the result
print(f"Probability of exactly {k} fraudulent transactions: {probability:.6f}")
