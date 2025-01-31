from scipy.stats import binom

# Define parameters
n = 50   # Total number of visitors
k = 5    # Number of visitors who make a purchase
p = 0.1  # Probability of a visitor making a purchase

# Calculate binomial probability P(X = 5)
probability = binom.pmf(k, n, p)

# Print result
print(f"Probability of exactly {k} visitors making a purchase: {probability:.4f}")
