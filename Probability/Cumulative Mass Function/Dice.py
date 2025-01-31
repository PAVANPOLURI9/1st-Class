import random

def roll_dice():
    return random.randint(1, 6)

def main():
    total = 0
    for _ in range(10):  # Roll the dice 10 times
        result = roll_dice()
        if result % 2 == 0:  # Check if the result is even
            total += result
            print(f"Rolled an even number: {result}, current total: {total}")
        else:
            print(f"Rolled an odd number: {result}, not added to total")
    print(f"Final total of even numbers: {total}")

if __name__ == "__main__":
    main()