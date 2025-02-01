from statistics import variance, stdev

# Sample data: Crop yield (in tons per hectare) for different crops in a field
crop_yields = {
    "Wheat": [2.1, 2.3, 2.5, 2.2, 2.4],
    "Corn": [3.5, 3.7, 3.8, 3.6, 3.9],
    "Rice": [4.2, 4.1, 4.3, 4.0, 4.4],
    "Barley": [1.8, 1.9, 2.0, 1.7, 2.1]
}

# Calculate variance and standard deviation for each crop
spread_results = {}
for crop, yields in crop_yields.items():
    var_value = variance(yields)
    std_dev_value = stdev(yields)
    spread_results[crop] = (var_value, std_dev_value)

# Display results
print("Spread Analysis of Crop Yields:")
for crop, (var_value, std_dev_value) in spread_results.items():
    print(f"{crop}: Variance = {var_value:.2f}, Standard Deviation = {std_dev_value:.2f}")
