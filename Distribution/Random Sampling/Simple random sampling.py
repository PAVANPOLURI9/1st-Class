import random

def select_passengers_for_screening(passenger_list, num_selected):
    """
    Selects a random subset of passengers for additional screening.
    
    :param passenger_list: List of passenger names or IDs.
    :param num_selected: Number of passengers to be screened.
    :return: List of selected passengers.
    """
    if num_selected > len(passenger_list):
        return "Error: More passengers selected than available."
    
    selected_passengers = random.sample(passenger_list, num_selected)
    return selected_passengers

# Example passenger list
passengers = ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown", "Charlie Davis", "David Lee", "Eve Adams", "Frank White"]

# Number of passengers to be randomly selected for screening
num_to_screen = 3

# Run the selection process
selected = select_passengers_for_screening(passengers, num_to_screen)

# Output results
print("Passengers selected for additional screening:")
for passenger in selected:
    print(passenger)
