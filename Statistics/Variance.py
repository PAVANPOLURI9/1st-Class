from statistics import variance, stdev

# Sample data: Magnitude of earthquakes recorded in a region over a period
earthquake_magnitudes = [4.1, 3.8, 5.2, 4.5, 4.9, 5.1, 3.7, 4.4, 5.3, 4.0]

# Calculate variance and standard deviation
var_value = variance(earthquake_magnitudes)
std_dev_value = stdev(earthquake_magnitudes)

# Display results
print("Earthquake Magnitude Spread Analysis:")
print(f"Variance: {var_value:.2f}")
print(f"Standard Deviation: {std_dev_value:.2f}")
