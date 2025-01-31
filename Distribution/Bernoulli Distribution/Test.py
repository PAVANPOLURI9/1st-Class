import numpy as np

# Define probability of passing
p_pass = 0.7  # 70% chance of passing

# Simulate a single Bernoulli trial (1 = Pass, 0 = Fail)
result = np.random.choice([1, 0], p=[p_pass, 1 - p_pass])

# Print result
print("Pass" if result == 1 else "Fail")
