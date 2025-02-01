def calculate_mean(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

# Example: Calculate the mean working hours of an employee in construction over a week
working_hours = [8, 9, 7.5, 8.5, 8, 7, 6]  # Hours worked each day from Monday to Sunday
mean_hours = calculate_mean(working_hours)

print(f"The mean working hours of the employee over the week is: {mean_hours} hours")