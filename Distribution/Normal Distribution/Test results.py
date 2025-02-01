import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Parameters for Normal Distribution
mean = 70  # Average exam score
std_dev = 10  # Standard deviation of exam scores
num_samples = 1000  # Number of students

# Generate random data following a normal distribution
exam_scores = np.random.normal(loc=mean, scale=std_dev, size=num_samples)

# Plot the distribution
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.histplot(exam_scores, kde=True, bins=30, color='blue', stat='density')
plt.title('Normal Distribution of Exam Scores')
plt.xlabel('Exam Scores')
plt.ylabel('Density')
plt.show()
