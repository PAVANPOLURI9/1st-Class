def calculate_median_with_outlier(data):
    # Sort the data
    sorted_data = sorted(data)
    
    # Calculate the median
    n = len(sorted_data)
    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    
    return median

# Example data for shipping capacity with an outlier
shipping_capacity = [100, 200, 300, 400, 500, 10000]  # 10000 is an outlier

median_capacity = calculate_median_with_outlier(shipping_capacity)
print(f"The median shipping capacity is: {median_capacity}")