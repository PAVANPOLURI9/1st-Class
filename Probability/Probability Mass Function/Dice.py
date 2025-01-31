import numpy as np
import matplotlib.pyplot as plt

# Define the range of values for a fair six-sided die
possible_outcomes = np.arange(1, 7)  # Dice values: 1 to 6
probability = 1 / len(possible_outcomes)  # Uniform probability

# Compute the probability mass function (PMF)
pmf_values = np.full_like(possible_outcomes, probability, dtype=float)

# Plot the probability mass function
plt.bar(possible_outcomes, pmf_values, width=0.3, color='blue', alpha=0.7, edgecolor='black')
plt.xlabel("Dice Outcome")
plt.ylabel("Probability Mass")
plt.title("Probability Mass Function for a Fair Dice")
plt.xticks(possible_outcomes)
plt.ylim(0, 0.2)
plt.show()
