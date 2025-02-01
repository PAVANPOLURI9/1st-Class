import numpy as np
import pandas as pd
import random

def cluster_sampling(data, num_clusters):
    """
    Perform cluster sampling by randomly selecting entire clusters.
    
    :param data: DataFrame containing the population.
    :param num_clusters: Number of clusters to select.
    :return: Sampled DataFrame with selected clusters.
    """
    # Identify unique clusters
    clusters = data["Cluster"].unique()
    
    # Randomly select clusters
    selected_clusters = random.sample(list(clusters), num_clusters)
    
    # Filter data to include only the selected clusters
    sampled_data = data[data["Cluster"].isin(selected_clusters)]
    
    return sampled_data

# Example dataset (20 individuals divided into 5 clusters)
data = pd.DataFrame({
    "ID": np.arange(1, 21),
    "Age": np.random.randint(18, 60, size=20),
    "Cluster": np.repeat(["A", "B", "C", "D", "E"], 4)  # 5 clusters (A-E), each with 4 members
})

# Define number of clusters to select
num_clusters = 2  # Selecting 2 clusters

# Perform cluster sampling
cluster_sample = cluster_sampling(data, num_clusters)

# Display result
print("Cluster Sample:")
print(cluster_sample)
