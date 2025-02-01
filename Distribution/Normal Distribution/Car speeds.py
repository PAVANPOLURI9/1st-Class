import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Parameters for Normal Distribution (Car Speeds)
mean_speed = 60  # Speed limit in mph
std_dev = 5  # Standard deviation (cars are typically within 5 mph of the speed limit)
num_cars = 1000  # Number of cars

# Generate random data for car speeds following a normal distribution
car_speeds = np.random.normal(loc=mean_speed, scale=std_dev, size=num_cars)

# Plotting the distribution of car speeds
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.histplot(car_speeds, kde=True, bins=30, color='blue', stat='density')

# Customize the plot
plt.title('Speed Distribution of Cars on the Highway')
plt.xlabel('Speed (mph)')
plt.ylabel('Density')
plt.axvline(mean_speed, color='red', linestyle='dashed', linewidth=2, label='Mean Speed (60 mph)')
plt.legend()

# Show plot
plt.show()
