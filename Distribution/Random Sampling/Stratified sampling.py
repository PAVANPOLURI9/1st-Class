import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit

# Sample dataset (e.g., survey respondents with different age groups)
data = {
    "ID": np.arange(1, 21),  # 20 respondents
    "Age Group": ["18-25"] * 5 + ["26-35"] * 6 + ["36-50"] * 4 + ["50+"] * 5,
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Define stratified sampling strategy (select 40% of the data)
split = StratifiedShuffleSplit(n_splits=1, test_size=0.4, random_state=42)

# Perform stratified sampling
for train_idx, sample_idx in split.split(df, df["Age Group"]):
    stratified_sample = df.iloc[sample_idx]

# Display the sampled data
print("Stratified Sample:")
print(stratified_sample)
