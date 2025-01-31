from scipy.stats import binom

# Define parameters
n = 942000   # Total number of unemployed people surveyed
k = 268000    # Number of people who apply for benefits
p = 0.42    # Probability of applying for benefits

# Calculate binomial probability P(X = 600000)
probability = binom.pmf(k, n, p)

# Print result
print(f"Probability of exactly {k} people applying for benefits: {probability:.6f}")
