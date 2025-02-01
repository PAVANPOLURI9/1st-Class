import numpy as np
import pandas as pd

def systematic_sampling(data, sample_size):
    """
    Perform systematic sampling on a dataset.
    
    :param data: List or DataFrame containing the population.
    :param sample_size: Number of samples to select.
    :return: Systematically selected sample.
    """
    population_size = len(data)
    interval = population_size // sample_size  # Step size (k)
    
    # Random starting point
    start = np.random.randint(0, interval)
    
    # Select every k-th element
    sample = data.iloc[start::interval]
    
    return sample

# Example dataset (Population of 20 individuals)
data = pd.DataFrame({
    "ID": np.arange(1, 21),  # IDs from 1 to 20
    "Age": np.random.randint(18, 60, size=20)  # Random ages
})

# Define sample size
sample_size = 5

# Perform systematic sampling
systematic_sample = systematic_sampling(data, sample_size)

# Display result
print("Systematic Sample:")
print(systematic_sample)
