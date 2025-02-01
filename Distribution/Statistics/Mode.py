from collections import Counter

def calculate_mode(checkups):
    if not checkups:
        return None
    count = Counter(checkups)
    mode = count.most_common(1)[0][0]
    return mode

# Example usage
checkups = [3, 4, 2, 3, 5, 3, 4, 2, 3, 4, 4]
mode_checkups = calculate_mode(checkups)
print(f"The mode of the number of checkups is: {mode_checkups}")