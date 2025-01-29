import numpy as np
import matplotlib.pyplot as plt

# Define the range of values for a fair six-sided die
possible_outcomes = np.arange(1, 7)  # Dice values: 1 to 6
probability = 1 / len(possible_outcomes)  # Uniform probability

# Define the range of interest (2 to 5)
selected_outcomes = np.arange(2, 6)
selected_probabilities = np.full_like(selected_outcomes, probability, dtype=float)

# Plot the probability density function
plt.bar(selected_outcomes, selected_probabilities, width=0.5, color='blue', alpha=0.7, edgecolor='black')
plt.xlabel("Dice Outcome")
plt.ylabel("Probability Density")
plt.title("Probability Density Function for Dice Outcomes (2 to 5)")
plt.xticks(selected_outcomes)
plt.ylim(0, 0.2)
plt.show()
