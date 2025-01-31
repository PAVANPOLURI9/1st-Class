import pandas as pd
import numpy as np

def convenience_sampling(data, sample_size):
    """
    Perform convenience sampling by selecting the first 'sample_size' number of individuals.
    
    :param data: DataFrame containing the population.
    :param sample_size: Number of samples to select.
    :return: Sampled DataFrame.
    """
    # Select the first 'sample_size' individuals from the data
    sample = data.head(sample_size)
    
    return sample

# Example dataset (20 individuals with random ages)
data = pd.DataFrame({
    "ID": np.arange(1, 21),
    "Age": np.random.randint(18, 60, size=20)
})

# Define sample size (e.g., take 5 people for convenience sampling)
sample_size = 5

# Perform convenience sampling
convenience_sample = convenience_sampling(data, sample_size)

# Display result
print("Convenience Sample:")
print(convenience_sample)
