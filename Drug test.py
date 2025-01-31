from scipy.stats import binom

# Define parameters
n = 20  # Total number of patients
k = 15  # Number of recovered patients
p = 0.7  # Probability of success (recovery)

# Calculate binomial probability P(X = 15)
probability = binom.pmf(k, n, p)

# Print result
print(f"Probability of exactly {k} patients recovering: {probability:.4f}")
